[![Continuous Integration](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/dependabot.yml/badge.svg)](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/dependabot.yml)
<br/><br/>
<h1 align="center">
📲📩
<br/><br/>
</h1>

**Bulk SMS Sender** is a web-based application that leverages a Twilio account to send SMS messages in bulk using a CSV file. This file can be uploaded via a web form or fetched from a provided URL. 

🚨 **_Please note, this project is not supported or endorsed by Twilio Inc. in any way._**

## 📖 Table of Contents
- [🧑‍💻 Usage](#-usage)
- [⚙️ Configuration](#️-configuration)
- [🚀 Deployment](#-deployment)
- [🛠️ Tech Stack](#️-tech-stack)

## 🧑‍💻 Usage

Input your Twilio credentials and either upload a CSV file or provide a CSV URL via a web form. The backend employs Twilio's Python SDK to send the messages and generate a delivery report. 

## ⚙️ Configuration

You can preset the Twilio credentials and CSV URL by setting the environment variables `TWILIO_SID`, `TWILIO_TOKEN`, and `CSV_URL`. When set, these values will be used as defaults in the web form. 

## 🚀 Deployment

[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/RAHB-REALTORS-Association/sms-sender/tree/master)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/RAHB-REALTORS-Association/sms-sender/tree/master)

Before deploying, review the `settings.py`, especially the following settings:

- Line 2: Testing
- Line 3: Flask secret. Generate a random Secret on deployment.
- Line 6: Set the upload folder according to your OS.

Remember to set the `TWILIO_SID`, `TWILIO_TOKEN`, and `CSV_URL` environment variables if you want to preset these values.

## 🛠️ Tech Stack

The technologies employed in this project include:

- Python 3.9 - 3.11 🐍
- Flask 2.3+ 🌐
- GUnicorn 21.2+ 🦄
- Twilio Python Libraries 8.5+ 📚
