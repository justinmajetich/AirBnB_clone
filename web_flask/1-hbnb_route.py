#!/usr/bin/python3
""" a script that starts a Flask web application
"""
from flask import Flask
app = Flash(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ A function that display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ A function that display HBNB """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
