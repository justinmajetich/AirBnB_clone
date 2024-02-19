#!/usr/bin/python3
"""6-number_odd_or_even module
Starts a Flask web application
"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """Return: HTML page only if n is integer"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_parity(n):
    """Return: HTML page only if n is integer
    H1 tag: Number: n is even|odd
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
