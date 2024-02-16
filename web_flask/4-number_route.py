#!/usr/bin/python3
"""hello_route
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display hello message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display():
    """Display 'HBNB' """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Display input values

    :param value: value in URL
    :type value: str, int
    :return: a string
    :rtype: str
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display_text_1(text):
    """ Display input text

    :param text: text in URL
    :type text: str
    :return: a string
    :rtype: str
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Display number

    :param n: number in URL
    :type n: str
    :return: a string
    :rtype: str
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
