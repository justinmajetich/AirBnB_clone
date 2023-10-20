#!/usr/bin/python3
"""
This module define a flask web framework with a route
"""
from flask import Flask, request, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ define a number n if n is an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ define template number """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
