#!/usr/bin/python3
"""Starts a web application."""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def helloHBNB():
    """returns Hello HBN!."""
    return ("Hello HNBN!")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
