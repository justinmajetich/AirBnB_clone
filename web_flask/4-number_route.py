#!/usr/bin/python3
"""4-number_route module
Starts a Flask web application"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Return: Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Return: HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """Return: C text"""
    return "C %s" % text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """Return: Python text"""
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """Return: n is a number if n is int"""
    return "%s is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0')
