#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ Return Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Show HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Show C with value of variable """
    return 'C ' + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_route(text="is cool"):
    """ display Python, and variable """
    return "Python" + " " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Displays n is a number only if n is an integer"""
    if type(n) == int:
        return str(n) + " is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
