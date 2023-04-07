#!/usr/bin/python3
""" This script starts a web flask application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns a string containing "Hello HBNB!" when called.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns a string containing "HBNB" when called.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    This function returns a string containing "C " followed by the value
      of the text variable with underscores replaced with spaces when called.
    """
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
