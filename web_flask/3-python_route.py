#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    if "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/python", strict_slashes=False)
def python_default():
    return f"Python is cool"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
