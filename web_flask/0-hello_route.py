#!/usr/bin/python3
"""
scripts to start flask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns hello holberton"""
    hello = 'Hello HBNB!'
    return (hello)


if __name__ == '__main__':
    app.run()
