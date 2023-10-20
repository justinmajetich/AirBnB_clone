#!/usr/bin/python3
"""
this is a simple Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    """Display  'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Display 'C' followed by the text."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text):
    """Display 'Python' followed by the text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Display n is a number only if n is int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer."""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return render_template("6-number_odd_or_even.html",
                           number=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
