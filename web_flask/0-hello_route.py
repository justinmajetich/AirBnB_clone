#!/usr/bin/python3
from flask import Flask

"""Importing the flask module"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """A funtion that defines a return value."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
