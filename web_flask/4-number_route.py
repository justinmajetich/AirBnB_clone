#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns hello hbnb"""
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Retturns C and the text that follows"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Returns Python an the text that follows"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Returns a number only if it is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
