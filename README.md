[![Continuous Integration](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/dependabot.yml/badge.svg)](https://github.com/RAHB-REALTORS-Association/sms-sender/actions/workflows/dependabot.yml)
<br/>
<p align="center">
<img src="https://raw.githubusercontent.com/RAHB-REALTORS-Association/sms-sender/master/docs/screenshots/screenshot.png" alt="Screenshot" width="600"/>
</p>

**Bulk SMS Sender** is a web-based application that leverages a Twilio account to send SMS messages in bulk using a CSV file. This file can be uploaded via a web form or fetched from a provided URL. 

🚨 **_Please note, this project is not supported or endorsed by Twilio Inc. in any way._**

## 📖 Table of Contents
- [⚙️ Configuration](#️-configuration)
- [🚀 Deployment](#-deployment)
- [🧑‍💻 Usage](#-usage)
- [🛠️ Tech Stack](#️-tech-stack)
- [🌐 Community](#-community)

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

## 🧑‍💻 Usage

### Setting up the list of contacts and message

Now we'll use a spreadsheet software (like Excel) to create a list of contacts and messages that we'll use to send the SMS. I've done this example using Google Sheets but any software will do (Excel, Numbers, LibreOffice, etc):

1. Open your spreadsheet software and start by entering your Twilio phone number on the first cell (A1).
2. In the next column (B1) you enter the destination phone number. Make sure to include country and area code.
3. In the third column (C1) you enter the message you want to send.

That's it! You can copy and paste the message and Twilio phone number to all other rows if they are the same and just fill the B column with your destination phone numbers.Sample sheet

![screenshot](https://github.com/RAHB-REALTORS-Association/sms-sender/blob/master/static/tutorial_003.png?raw=true)

### Export the file and upload it

Now you just need to save your spreadsheet in the format this app can use and upload it. How to do that might differ a bit from app to app:

- **Google Sheets:** click on "File", "Download", "Comma-separated values (.csv, current sheet)
- **Excel:** click on "File" and then in "Save as". On the "File Format" box select "Comma Separated Values (.csv)"
- **Numbers for Mac:** click on "File", "Export to", "CSV" and proceed to save the file
- **OpenOffice:** click on "File", "Save as" and set "File type" as "Text CSV (.csv)"

Once you have you file ready go back to our home page and use the form at the bottom to upload your file and Twilio credentials. That's it! If everything is alright we'll start sending your messages and once we are done we'll show you a full report, so please be patient!

## 🛠️ Tech Stack

The technologies employed in this project include:

- Python 3.9 - 3.11 🐍
- Flask 2.3+ 🌐
- GUnicorn 21.2+ 🦄
- Twilio Python Libraries 8.5+ 📚

## 🌐 Community

### Contributing 👥🤝

We welcome contributions to the Bulk SMS Sender project. Every contribution, regardless of its scale, is appreciated. For our Code of Conduct, see [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

To get started, fork the repo, make your changes, and then push your code to open a pull request. If you're new to GitHub or open source, [this guide](https://www.freecodecamp.org/news/how-to-make-your-first-pull-request-on-github-3#let-s-make-our-first-pull-request-) or the [git docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) may be helpful, but don't hesitate to ask if you need assistance.

[![Submit a PR](https://img.shields.io/badge/Submit_a_PR-GitHub-%23060606?style=for-the-badge&logo=github&logoColor=fff)](https://github.com/RAHB-REALTORS-Association/sms-sender/compare)

### Reporting Bugs 🐛📝

If you encounter an issue or want to suggest a new feature, please raise an issue on GitHub. For bugs, please provide the steps to reproduce and include any relevant information like system info and resulting logs.

[![Raise an Issue](https://img.shields.io/badge/Raise_an_Issue-GitHub-%23060606?style=for-the-badge&logo=github&logoColor=fff)](https://github.com/RAHB-REALTORS-Association/sms-sender/issues/new/choose)
