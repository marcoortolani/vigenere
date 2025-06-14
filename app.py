from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/cipher", methods=["GET", "POST"])
def vig_cipher():
    submitted_text = None
    if request.method == "POST":
        submitted_text = request.form.get("user_input")
    return render_template("cipher.html", text=submitted_text, title="Vigenere Cipher")

@app.route('/welcome-astronaut')
def welcome_astronaut():
    return 'Welcome to the Interstellar Space Station!'
