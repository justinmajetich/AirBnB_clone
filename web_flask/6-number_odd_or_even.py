#!/usr/bin/python3
"""
This module starts a Flask web application.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Displays "Hello HBNB!" on the main page.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Displays "C" followed by the text in <text>. All
    underscores replaced with whitespace.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """
    Displays "Python" followed by the text in <text>. If
    no text is provided, default is "is cool". All
    underscores replaced with whitespace.
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Displays the text "is a number" after the number <n>,
    but only if <n> is an integer.
    """
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Displays the HTML template if the number <n> is an integer.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    Displays the HTML template if the number <n> is an integer.
    Text in template will reflect if int is odd or even.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
