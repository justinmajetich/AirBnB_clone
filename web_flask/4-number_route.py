#!/usr/bin/python3
"""
Script that starts a Flask application.
"""
from flask import Flask
from flask import abort


APP = Flask(__name__)


@APP.route("/", strict_slashes=False)
def hello_holberton():
    """
    Returns 'Hello HBNB!'.
    """
    return "Hello HBNB!"

@APP.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB'.
    """
    return "HBNB"

@APP.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """
    Returns C, followed by text value.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

@APP.route("/python", strict_slashes=False)
@APP.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """
    Returns Python, followed by text value.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@APP.route("/number/<int:n>", strict_slashes=False)
def IsINT(n):
    """
    Returns n is a number if n is a integer.
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port="5000")
