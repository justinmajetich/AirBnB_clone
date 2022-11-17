#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
from sys import argv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """
    Returns `Hello HBNB!`.
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """
    Returns `HBNB`
    """
    return "HBNB"


@app.route("/c/<text>")
def c_is_cool(text):
    """
    Returns `C` followed by the value of the
    `text` variable (replace `_` symbols with
    a space ` `.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    Returns `Python ` followed by the value of
    the `text` variable (replace `_` symbols
    with a space ` `.
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
