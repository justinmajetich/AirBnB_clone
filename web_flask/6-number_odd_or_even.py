#!/usr/bin/python3
"""Starts a Flask web application that
accepts a route with a variable and checks
if variable is an integer"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_text(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    if n % 2 is 0:
        return render_template("6-number_odd_or_even.html",
                               n="{} is even".format(n))
    return render_template("6-number_odd_or_even.html",
                           n="{} is odd".format(n))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
