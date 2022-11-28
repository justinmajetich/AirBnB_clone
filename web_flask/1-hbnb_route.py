#!/usr/bin/python3
"""
Script that starts a Flask application.
"""
from flask import Flask


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

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port="5000")
