import os
# Flask config
TESTING = False
SECRET_KEY = os.environ.get('SECRET_KEY')
TWILIO_SID = os.environ.get('TWILIO_SID', '')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN', '')
CSV_URL = os.environ.get('CSV_URL', '')
PERMANENT_SESSION_LIFETIME = 180
JSONIFY_PRETTYPRINT_REGULAR = True
UPLOAD_FOLDER = "/tmp"
ALLOWED_EXTENSIONS = {"csv"}
LOG_FILE = "sms-log.txt"
