#!/usr/bin/python3
""" hello and hbnb route module """
from flask import Flask
from os import environ
app = Flask(__name__)
environ.FLASK_APP = '3-python_route.py'


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

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text='is cool'):
    return 'Python {}'.format(text.replace('_', " "))

if __name__ == '__main__':
	app.run(host='0.0.0.0')
