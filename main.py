import os
from datetime import datetime

from flask import Flask, request, flash, redirect, render_template, send_from_directory
from werkzeug.utils import secure_filename

import tools
import settings

application = Flask(__name__)
application.config.from_object("settings")


@application.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(application.static_folder, request.path[1:])


@application.route("/instructions")
def instructions():
    return render_template("instructions.html")


@application.route("/contact")
def contact():
    return render_template("contact.html")


@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form["sid"] == "" or request.form["token"] == "":
            flash("Twilio ID and token required")
            return redirect(request.url)

        sid = request.form["sid"]
        token = request.form["token"]

        if not tools.valid_credentials(sid, token):
            flash("Invalid Twilio credentials. Please double check your Twilio account SID and token and try again")
            return redirect(request.url)

        if "file" not in request.files:
            flash("No file selected")
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)

        if file and tools.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(
                os.path.join(
                    application.config["UPLOAD_FOLDER"],
                    filename
                )
            )

            number_list = tools.get_number_list(filename)
            wrong_numbers = tools.check_numbers(number_list, sid, token)

            if wrong_numbers:
                with open(settings.LOG_FILE, "a") as log_file:
                    log_string = f"{datetime.now()} - {len(wrong_numbers)} wrong numbers identified."
                    log_file.write(f"\n{log_string}")
                return render_template(
                    "wrong_numbers.html",
                    number_list=wrong_numbers
                )

            number_list = tools.send_messages(number_list, sid, token)
            return render_template("report.html", number_list=number_list)
        else:
            flash("File type not allowed. Please select a CSV file")
            return redirect(request.url)

    return render_template("index.html")
