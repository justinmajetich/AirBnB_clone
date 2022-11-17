#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from sys import argv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """
    Returns `Hello HBNB!`.
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """
    Returns `HBNB`
    """
    return "HBNB"


@app.route("/c/<text>")
def c_is_cool(text):
    """
    Returns `C` followed by the value of the
    `text` variable (replace `_` symbols with
    a space ` `.
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    Returns `Python ` followed by the value of
    the `text` variable (replace `_` symbols
    with a space ` `.
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def is_number(n):
    """
    Returns ``n` is a number` only if `n` is
    an integer.
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def html_if_num(n):
    """
    Returns an html page containing `n` if `n`
    is an integer.
    """
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """
    Returns an html page containing `{n} is even`
    if `n` is an even integer, or `{n} is odd` if
    `n` is an odd integer.
    """
    return render_template('6-number_odd_or_even.html', num=n,
                           isOE=("even" if n % 2 == 0 else "odd"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
