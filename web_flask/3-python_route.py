#!/usr/bin/python3
"""
This module define a flask web framework with a route
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """This function define the route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Define C text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Define Python text with default value 'is cool'"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
