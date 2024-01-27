#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C followed by text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", default={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Display Python followed by text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
