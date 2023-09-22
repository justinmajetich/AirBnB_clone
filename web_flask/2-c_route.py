#!/usr/bin/python3
"""Starts Flask web app
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays 'C' followed by the value <text>."""
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
