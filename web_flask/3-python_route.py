#!/usr/bin/python3
""" This script starts at any ip address of 0.0.0.0 in port 5000 """
from flask import Flask


apt = Flask(__name__)


@apt.route('/', strict_slashes=False)
def hello():
    """ This function simply renders the string 'Hello HBNB' """
    return ('Hello HBNB!')


@apt.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Rendering a string 'HBNB' """
    return 'HBNB'


@apt.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Rendering a variable and replacing '_' with space """
    text = text.replace('_', ' ')
    return 'C %s' % text


@apt.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@apt.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    apt.run(host='0.0.0.0', port=5000)
