#!/usr/bin/python3
""" hello and hbnb route module """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_():
    """ Displays hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
def hello_python(text='is cool'):
    return 'Python {}'.format(text.replace('_', " "))
