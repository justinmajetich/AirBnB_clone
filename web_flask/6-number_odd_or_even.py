#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ Returns Hello HBNB! from 0.0.0.0:5000 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns HBNB from 0.0.0.0:5000/hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Script displays the value of text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """method displays text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    """Return n if n is an int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """method renders an HTML page"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    """Script displays a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
