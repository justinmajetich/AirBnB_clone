#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route():
    """Return two words"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    """Return a word"""
    return "HBNB"


@app.route('/c/<path:subpath>', strict_slashes=False)
def route_c(subpath):
    """Return subpath"""
    return "C {}".format(escape(subpath).replace('_', ' '))


@app.route('/python', defaults={'subpath': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:subpath>', strict_slashes=False)
def route_python(subpath):
    """Return subpath"""
    return "Python {}".format(escape(subpath).replace('_', ' '))


@app.route('/number/<int:num>', strict_slashes=False)
def route_number(num):
    """Return only if num is a int"""
    return "{} is a number".format(escape(num))


@app.route('/number_template/<int:num>', strict_slashes=False)
def route_template(num):
    """Return a file HTML only if num is a int"""
    return render_template("5-number.html", n=num)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
