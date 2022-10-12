***Notice: this project is not supported or endorsed by Twilio Inc. in any way***

# Bulk SMS Sender

## About
Bulk SMS Sender is a web-based app that uses a Twilio account to send SMS messages in bulk from a CSV file.

## Usage
The user saves the data on a CSV file with 3 columns and use a webform to update the CSV file with their Twilio credentials. The backend uses
Twilio's Python SDK to send the messages and generate a delivery report. A deployed version can be found [here](https://twilio-app-23959-bp79h.ondigitalocean.app).

## Tech stack
- Python 3.8
- Flask 1.1.2
- GUnicorn 20.0.4
- Twilio Python Libraries 6.46.0

## Deploying
Review settings.py before deployment, especially the following settings:
- Line 2: Testing
- Line 3: Flask secret. Generate a random Secret on deployment
- Line 6: Set the upload folder according to your OS
