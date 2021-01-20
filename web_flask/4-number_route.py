#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Displays hello message
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Displays the name
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text):
    """
        Displays C with custom text
    """
    return "C %s" % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>/', strict_slashes=False)
def pythonroute(text='is_cool'):
    """
        Displays Python with custom text
    """
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        Displays number if it is of type int
    """
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0')
