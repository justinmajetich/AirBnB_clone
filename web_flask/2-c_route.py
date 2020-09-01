#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Print a str
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """
    Print a str
    """
    return 'HBNB'


@app.route('/c/is_fun', strict_slashes=False)
def is_fun():
    """
    Print a str
    """
    return 'C is fun'


@app.route('/c/cool', strict_slashes=False)
def cool():
    """
    Print a str
    """
    return 'C cool'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")