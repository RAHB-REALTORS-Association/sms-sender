import csv
import os
import chardet
import logging
import requests
from datetime import datetime

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException, TwilioException
from urllib3.util import parse_url
from io import StringIO

import settings

# Setup logging
logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in settings.ALLOWED_EXTENSIONS
    )

def valid_credentials(sid, token):
    client = Client(sid, token)
    try:
        client.messages.list(limit=1)
    except TwilioException as e:
        logging.error(f"Error occurred in valid_credentials: {e}")
        return False
    return True

def is_valid_url(url):
    # Check if the URL has a valid format
    try:
        result = parse_url(url)
        if not all([result.scheme, result.netloc]):
            return False
    except ValueError:
        return False

    # Check if the URL is accessible
    try:
        response = requests.head(url)
        if response.status_code >= 400:
            return False
    except requests.RequestException:
        return False

    # Check if the response contains ASCII text
    response = requests.get(url)
    content_type = response.headers.get('Content-Type', '')
    if 'text' not in content_type:
        return False

    return True

def check_numbers(numbers, sid, token):
    client = Client(sid, token)
    numbers_not_found = list()
    for number in numbers:
        try:
            client.lookups.phone_numbers(number[1]).fetch()
        except TwilioRestException as e:
            logging.error(f"Error occurred in check_numbers: {e}")
            numbers_not_found.append(number)
    return numbers_not_found

def get_number_list_from_url(url):
    # Use requests to fetch the CSV data from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Convert the CSV data into a list of lists
    from io import StringIO
    csv_data = StringIO(response.text)
    try:
        csv_reader = csv.reader(csv_data)
        number_list = [row[:3] for row in csv_reader]  # Only include the first three columns
    except csv.Error as e:
        logging.error(f"Invalid CSV data: {e}")
        raise ValueError("Invalid CSV data") from e

    return number_list

def get_number_list(filename):
    number_list = list()
    file_path = os.path.join(
        settings.UPLOAD_FOLDER,
        filename
    )

    # Routine to detect CSV file encoding
    rawdata = open(file_path, "rb").read()
    guessed_encoding = chardet.detect(rawdata)

    with open(
            file_path,
            newline="",
            mode="r",
            encoding=guessed_encoding["encoding"]) as csv_file:
        csv_reader = csv.reader(csv_file)
        number_list = [row[:3] for row in csv_reader]  # Only include the first three columns
    os.remove(file_path)
    return number_list

def send_messages(number_list, sid, token):
    client = Client(sid, token)
    flag = 0
    while flag < len(number_list):
        try:
            sender_chars = [c for c in number_list[flag][0]]
            logging.info(f"Sending message to: {number_list[flag][1]}")
            message = client.messages.create(
                body=number_list[flag][2],
                from_=number_list[flag][0],
                to=number_list[flag][1]
            )
            number_list[flag].append(message.status)
            number_list[flag].append(message.sid)
            flag += 1
        except TwilioRestException as e:
            logging.error(f"Error occurred in send_messages: {e}")
            flag += 1  # Skip to the next number
    for item in number_list:
        try:
            current_message = client.messages.get(item[4]).fetch()
            item[3] = current_message.status
        except TwilioRestException as e:
            logging.error(f"Error occurred when fetching message status: {e}")
    with open(settings.LOG_FILE, "a") as log_file:
        log_string = f"{datetime.now()} - {len(number_list)} messages sent."
        log_file.write(f"\n{log_string}")
    return number_list
