from flask import Flask, render_template, request
from flask import url_for, send_file

import qrcode
import io
import os

from vigenere import casear_encrypt, encrypt, decrypt

app = Flask(__name__)

#############
# MAIN PAGE #
#############
@app.route("/", methods=["GET", "POST"])
def hello_world():
    submitted_text = None
    result_text = None


    if request.method == "POST":
        action = request.form.get("action")
        vig_key = load_key()
        submitted_text = request.form.get("user_input")

        if action == "encrypt":
            result_text = encrypt(submitted_text, vig_key)
        elif action == "decrypt":
            result_text = decrypt(submitted_text, vig_key)
        elif action == "clear":
            submitted_text = ""
            result_text = ""

    return render_template("index.html", user_text=submitted_text, processed_text=result_text, title="Vigenere")

###########
# QR CODE #
###########
@app.route("/qr")
def qr():
    # Get current page's URL
    full_url = request.args.get("data", request.url_root)
    # full_url = f"{request.scheme}://{host}{request.path}"

    codespace_name = os.environ.get("CODESPACE_NAME")
    port = 5000  # your app's port number

    if codespace_name:
        public_url = f"https://{codespace_name}-{port}.app.github.dev"
    else:
        public_url = full_url

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