#!/usr/bin/python3
"""
Script that runs a flask app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Function that returns on url
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_school():
    """
    Function that returns on url /hbnb
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
