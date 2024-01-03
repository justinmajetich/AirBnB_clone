#!/usr/bin/python3

"""
Simple Flask web app with a greeting route.
"""

from flask import Flask
""" Creates an application object """
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ returns Hello HBNB """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
