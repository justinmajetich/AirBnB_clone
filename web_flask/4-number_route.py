#!/usr/bin/python3
"""simple flask routes"""
from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return message HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """return message with paramns"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_fun(text):
    """return message with paramns"""
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """return message with paramns"""

    if n.isdigit():
        return "{} is a number".format(n)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
