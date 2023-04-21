#!/usr/bin/python3
"""
This module contains a Flask web application
that responds to HTTP requests with various messages.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Responds to a GET request with the message "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Responds to a GET request with the message "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Responds to a GET request with the
    message "C <text>", where <text> is
    the value of the 'text' URL parameter,
    with underscores replaced with spaces.
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
