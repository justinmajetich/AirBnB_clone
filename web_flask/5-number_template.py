#!/usr/bin/python3
"""
Importing the flask module
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """A funtion that defines a return value."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A function that returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """A function that returns text"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text="is cool"):
    """A function that returns text"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """A function that returns a number or not"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemplate(n):
    """A function that renders a template if n was int"""
    if isinstance(n, int):
        return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run()
