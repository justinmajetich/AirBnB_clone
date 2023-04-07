#!/usr/bin/python3
"""
This script starts a Flask web application that listens on port 5000
and displays "Hello HBNB!" when you visit the root URL
(/) and "HBNB" when you visit the /hbnb route.

Usage:
    $ python app.py

Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"

"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
