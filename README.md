***Notice: this project is not supported or endorsed by Twilio Inc. in any way***

# Bulk SMS Sender

## About
Bulk SMS Sender is a web-based app that uses a Twilio account to send SMS messages in bulk from a CSV file. This tool can be used by small
companies and practices that want to use SMS for campaings but doesn't have coding know-how.

## Usage
The user saves the data on a CSV file with 3 columns and use a webform to update the CSV file with their Twilio credentials. The backend uses
Twilio's Python SDK to send the messages and generate a delivery reported. A deployed version can be found [here](https://www.batchsms.eu)

## Tech stack
- Python 3.8
- Flask 1.1.2
- GUnicorn 20.0.4
- Twilio Python Libraries 6.46.0

## Deploying
Review settings.py before deployment, specially the following settings:
- Line 2: Testing
- Line 3: Flask secret. Generate a random Secret on deployment
- Line 6: Set the upload folder according to your OS
