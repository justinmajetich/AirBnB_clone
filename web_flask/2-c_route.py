#!/usr/bin/Python3

"""
This script starts a Flask web application that listens on port 5000 and displays various messages when you visit different routes.

Usage:
    $ python app.py

Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C " followed by the value of the text variable (replace underscore _ symbols with a space)

"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    