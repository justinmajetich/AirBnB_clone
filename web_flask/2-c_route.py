#!/usr/bin/python3
"""
The scripts starts a Flask WebAPP
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=True)
def cIsfun(text):
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
