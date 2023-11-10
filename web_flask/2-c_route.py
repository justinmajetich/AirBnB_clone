#!/usr/bin/python3
"""Script that starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    c_text = text.replace('_', ' ')
    return f'C {c_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
