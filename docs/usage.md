---
title: "🧑‍💻 Usage"
layout: page
nav_order: 3
---

# 🧑‍💻 Usage

## Setting up the list of contacts and message

Now we'll use a spreadsheet software (like Excel) to create a list of contacts and messages that we'll use to send the SMS. I've done this example using Google Sheets but any software will do (Excel, Numbers, LibreOffice, etc):

1. Open your spreadsheet software and start by entering your Twilio phone number on the first cell (A1).
2. In the next column (B1) you enter the destination phone number. Make sure to include country and area code.
3. In the third column (C1) you enter the message you want to send.

That's it! You can copy and paste the message and Twilio phone number to all other rows if they are the same and just fill the B column with your destination phone numbers.Sample sheet

![screenshot](https://github.com/RAHB-REALTORS-Association/sms-sender/blob/master/static/tutorial_003.png?raw=true)

## Export the file and upload it

Now you just need to save your spreadsheet in the format this app can use and upload it. How to do that might differ a bit from app to app:

- **Google Sheets:** click on "File", "Download", "Comma-separated values (.csv, current sheet)
- **Excel:** click on "File" and then in "Save as". On the "File Format" box select "Comma Separated Values (.csv)"
- **Numbers for Mac:** click on "File", "Export to", "CSV" and proceed to save the file
- **OpenOffice:** click on "File", "Save as" and set "File type" as "Text CSV (.csv)"

Once you have you file ready go back to our home page and use the form at the bottom to upload your file and Twilio credentials. That's it! If everything is alright we'll start sending your messages and once we are done we'll show you a full report, so please be patient!
