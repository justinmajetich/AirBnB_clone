#!/usr/bin/python3
"""Starts a web application."""


from tracemalloc import start
from flask import Flask


start = Flask(__name__)


@start.route("/", strict_slashes=False)
def helloHBNB():
    """returns Hello HBN!."""
    return ("Hello HNBN!")


if __name__ == "__main__":
    start.run()
