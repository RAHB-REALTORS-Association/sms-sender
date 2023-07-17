[![Pylint](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/pylint.yml/badge.svg?branch=master)](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/pylint.yml)[![Python 3.9](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/python-3.9.yml/badge.svg?branch=master)](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/python-3.9.yml)[![Python 3.10](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/python-3.10.yml/badge.svg?branch=master)](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/python-3.10.yml)[![Python 3.11](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/python-3.11.yml/badge.svg?branch=master)](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/python-3.11.yml)

***Notice: this project is not supported or endorsed by Twilio Inc. in any way***

# Bulk SMS Sender

## About
Bulk SMS Sender is a web-based app that uses a Twilio account to send SMS messages in bulk from a CSV file. The CSV file can be uploaded via a web form or fetched from a provided URL. 

## Usage
The user inputs their Twilio credentials and either uploads a CSV file or provides a CSV URL via a webform. The backend uses Twilio's Python SDK to send the messages and generate a delivery report.

## Configurability
The Twilio credentials and CSV URL can be preset using the following environment variables: `TWILIO_SID`, `TWILIO_TOKEN`, and `CSV_URL`. If these are set, their values will be used as defaults in the web form. 

## Tech stack
- Python 3.9 - 3.11
- Flask 2.2+
- GUnicorn 20.1+
- Twilio Python Libraries 7.14+

## Deploying

[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/RAHB-REALTORS-Association/sms-sender/tree/master)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/RAHB-REALTORS-Association/sms-sender/tree/master)

Review `settings.py` before deployment, especially the following settings:
- Line 2: Testing
- Line 3: Flask secret. Generate a random Secret on deployment
- Line 6: Set the upload folder according to your OS

Also remember to set the `TWILIO_SID`, `TWILIO_TOKEN`, and `CSV_URL` environment variables if you want to preset these values.
