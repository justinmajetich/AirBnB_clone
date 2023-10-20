#!/usr/bin/python3
"""
This script starts a Flask web application with different routes.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Route that displays "C ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """
    Route that displays "Python ", followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """
    Route that displays "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

