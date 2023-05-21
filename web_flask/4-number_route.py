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
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p3iscool(text='is cool'):
    """Function that displays "Python" followed by text variable."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes-False)
def isanum(n):
    """Function that returns "n is a number" if n is an integer."""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
