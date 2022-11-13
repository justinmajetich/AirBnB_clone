#!/usr/bin/python3
"""starts a Flask web application."""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def helloHBNB():
    """returns Hello HBNB!."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """returns HBNB."""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def variableValue(text):
    """returns the value of a variable."""
    return (
        'C %s' % escape(text.replace("_", " "))
    )


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def retPython(text="is cool"):
    """Display Python.

    Followed by the value of the text.
    """
    return (
        "Python %s" % escape(text.replace("_", " "))
    )


@app.route("/number/<int:n>", strict_slashes=False)
def isInt(n):
    """Display Int.

    Display the value of n if only is int.
    """
    return (n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
