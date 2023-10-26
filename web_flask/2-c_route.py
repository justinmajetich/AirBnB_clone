#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Routes:
    /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def air():
    """
    /: display “Hello HBNB!”
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    """
    /c/<text>: display “C ” followed by the value of the text variable
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
