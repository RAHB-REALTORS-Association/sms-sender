---
title: "🚀 Deployment"
layout: page
nav_order: 2
---

# 🚀 Deployment

[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/RAHB-REALTORS-Association/sms-sender/tree/master)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/RAHB-REALTORS-Association/sms-sender/tree/master)

Before deploying, review the `settings.py`, especially the following settings:

- Line 2: Testing
- Line 3: Flask secret. Generate a random Secret on deployment.
- Line 6: Set the upload folder according to your OS.

Remember to set the `TWILIO_SID`, `TWILIO_TOKEN`, and `CSV_URL` environment variables if you want to preset these values.
