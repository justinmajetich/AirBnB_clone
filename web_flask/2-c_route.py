#!/usr/bin/python3
"""Script that have 3 routes"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """replace _ for spaces"""
    text = text.replace('_', ' ')
    return f" C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)