#!/usr/bin/python3
"""Create flask app"""
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    """Home route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """C route"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def python_route(text):
    """Python route"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number_route(n):
    """Number route"""

    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
