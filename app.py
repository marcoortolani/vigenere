from flask import Flask, render_template, request
from flask import url_for, send_file

import qrcode
import io
import os

from vigenere import casear_encrypt, encrypt, decrypt

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/cipher", methods=["GET", "POST"])
def vig_cipher():
    submitted_text = None
    if request.method == "POST":
        submitted_text = request.form.get("user_input")

        shift_amount = 3
        encrypted_text = casear_encrypt(submitted_text, shift_amount)
        vig_key = "marco"
        encrypted_text = encrypt(submitted_text, vig_key)

    return render_template("cipher.html", text=encrypted_text, title="Vigenere Cipher")

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