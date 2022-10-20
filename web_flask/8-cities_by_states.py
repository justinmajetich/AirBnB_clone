#!/usr/bin/python3
"""This module uses Flask and starts a web application"""


from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello world for flask"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB for /hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """display `C` followed by value of text variable
    replace underscores with a space"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def py_route(text="is cool"):
    """display `Python` followed by value of text variable
    replace underscores with a space"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """display `n is a number` only if `n` is an int"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays a HTML page if `num` is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """displays a HTML page if `num` is an integer
    message on page changes depending on value passed"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays a HTML page of state objects present in DBstorage
    message on page changes depending on value passed"""
    return render_template('7-states_list.html', states=storage.all("State"))


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """displays a HTML page of city objects 
    in a nested list of state objects present in DBstorage
    message on page changes depending on value passed"""
    return render_template(
        '8-cities_by_state.html', states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)