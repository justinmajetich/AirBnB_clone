#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Funtion to print Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """print HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C {}".format(text).replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py(text='is cool'):
    """print python and the text"""
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """print n only if n is a number."""
    return "%d is a number" % n

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
