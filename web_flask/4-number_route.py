#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Routes:
    /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def air():
    """
    /: display “Hello HBNB!”
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    """
    /c/<text>: display “C ” followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    /python/<text>: display “Python ”, followed by the value of the text var
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    /number/<n>: display “n is a number” only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
