import csv
import os
import chardet
import logging
import requests
import re
from datetime import datetime
from urllib.parse import urlparse

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException, TwilioException

import settings

# Setup logging
logging.basicConfig(filename=settings.LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in settings.ALLOWED_EXTENSIONS

def valid_credentials(sid, token):
    client = Client(sid, token)
    try:
        client.messages.list(limit=1)
        return True
    except TwilioException as e:
        logging.error(f"Error occurred in valid_credentials: {e}")
        return False

def is_valid_url(url):
    # Regular expression for validating an URL
    regex = re.compile(
        # your existing regex pattern
    )

    # Validate URL format
    if not re.match(regex, url):
        return False

    try:
        parsed_url = urlparse(url)
        return all([parsed_url.scheme, parsed_url.netloc])
    except ValueError:
        return False

def check_numbers(numbers, sid, token):
    client = Client(sid, token)
    numbers_not_found = []
    for number in numbers:
        try:
            client.lookups.phone_numbers(number[1]).fetch()
        except TwilioRestException as e:
            logging.error(f"Error occurred in check_numbers: {e}")
            numbers_not_found.append(number)
    return numbers_not_found

def get_number_list_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        csv_data = StringIO(response.text)
        csv_reader = csv.reader(csv_data)
        return [row[:3] for row in csv_reader]
    except (requests.RequestException, csv.Error) as e:
        logging.error(f"Error in get_number_list_from_url: {e}")
        raise

def get_number_list(filename):
    file_path = os.path.join(settings.UPLOAD_FOLDER, filename)
    try:
        with open(file_path, "rb") as f:
            rawdata = f.read()
        guessed_encoding = chardet.detect(rawdata)['encoding']

        with open(file_path, newline="", mode="r", encoding=guessed_encoding) as csv_file:
            csv_reader = csv.reader(csv_file)
            return [row[:3] for row in csv_reader]
    finally:
        os.remove(file_path)

def send_messages(number_list, sid, token):
    client = Client(sid, token)
    for idx, number in enumerate(number_list):
        try:
            message = client.messages.create(body=number[2], from_=number[0], to=number[1])
            number.extend([message.status, message.sid])
        except TwilioRestException as e:
            logging.error(f"Error occurred in send_messages: {e}")
        # Update the status of each message
        try:
            current_message = client.messages.get(number[-1]).fetch()
            number[-2] = current_message.status
        except TwilioRestException as e:
            logging.error(f"Error occurred when fetching message status: {e}")

    log_string = f"{datetime.now()} - {len(number_list)} messages sent."
    logging.info(log_string)
    return number_list
