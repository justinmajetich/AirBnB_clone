#!/usr/bin/python3
"""
This module defines a Flask application with four routes:
- '/'
- '/hbnb'
- '/c/<text>'
- '/python/' (default value of 'text' is 'is cool')
- '/python/<text>'

The routes return strings based on the input text.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns a greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns the string 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Returns a string that prepends 'C ' to the given text.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Returns a string that prepends 'Python ' to the given text
    """
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
