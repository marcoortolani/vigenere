from flask import Flask, render_template, request
from flask import url_for, send_file

from urllib.parse import urlparse
import qrcode
import io
import os

from vigenere import vig_encrypt, vig_decrypt
from caesar import casear_encrypt

app = Flask(__name__)

#############
# HOME PAGE #
#############
@app.route("/")
def home():
    return render_template("index.html")

###############
# CAESAR TASK #
###############
@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    current_url = request.url  # full URL of current page

    submitted_text = None
    result_text = None


    if request.method == "POST":
        action = request.form.get("action")
        vig_key = load_key()
        submitted_text = request.form.get("user_input")

        if action == "encrypt":
            result_text = casear_encrypt(submitted_text, vig_key)
        elif action == "decrypt":
            result_text = casear_encrypt(submitted_text, vig_key)
        elif action == "clear":
            submitted_text = ""
            result_text = ""

    return render_template("caesar.html", user_text=submitted_text, processed_text=result_text, title="Caesar cipher", url=current_url)

###############
# CAESAR TASK #
###############
@app.route("/vigenere1", methods=["GET", "POST"])
def vigenere1():
    current_url = request.url  # full URL of current page

    submitted_text = None
    result_text = None


    if request.method == "POST":
        action = request.form.get("action")
        vig_key = load_key()
        submitted_text = request.form.get("user_input")

        if action == "encrypt":
            result_text = vig_encrypt(submitted_text, vig_key)
        elif action == "decrypt":
            result_text = vig_decrypt(submitted_text, vig_key)
        elif action == "clear":
            submitted_text = ""
            result_text = ""

    return render_template("vigenere1.html", user_text=submitted_text, processed_text=result_text, title="Vigenère cipher", url=current_url)

###########
# QR CODE #
###########
@app.route("/qr")
def qr():
    codespace_name = os.environ.get("CODESPACE_NAME")
    port = 5000  # your app's port number

    data_url = request.args.get("data", request.url)  # full URL passed as param or fallback

    if codespace_name:
        parsed = urlparse(data_url)
        current_path = parsed.path
        if parsed.query:
            current_path += "?" + parsed.query

        public_url = f"https://{codespace_name}-{port}.app.github.dev{current_path}"
    else:
        public_url = data_url

    # Generate QR code
    qr = qrcode.QRCode(
        version=5,                 # Increase from default (1). Max 40.
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,               # Size of each QR "box" in pixels (default 10 is fairly big)
        border=4                   # Border thickness in boxes
    )
    qr.add_data(public_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

#################
# OTHER METHODS #
#################
def load_key(filepath="key.txt"):
    try:
        with open(filepath, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "DEFAULTKEY"