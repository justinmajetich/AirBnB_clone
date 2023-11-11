#!/usr/bin/python3
"""Starts a Flask web app"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    formatted_text = text.replace('_', ' ')
    return "c {}".format(formatted_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
