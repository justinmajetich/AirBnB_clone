#!/usr/bin/python3
"""Module - script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles the root url"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
