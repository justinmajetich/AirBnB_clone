#!/usr/bin/python3
"""Script that starts the web app using flask."""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function that returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that returns HBNB."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def isfun(text):
    """Function that displays "C" followed by text variable."""
    return 'C' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
