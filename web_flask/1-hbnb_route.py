#!/usr/bin/python3
"""
Script that runs a flask app

"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Function that returns on url
    """
    return "Hello HBNB!"


@app.route('/', strict_slashes=False)
def hbnb():
    """
    Function that returns on url /hbnb

    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
