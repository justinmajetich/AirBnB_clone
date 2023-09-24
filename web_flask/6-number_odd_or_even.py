#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_start():
    """Function that displays HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """Function that displays 'C' followed by the value of <text>"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text="is cool"):
    """Function that displays 'python' followed by the value of <text>"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Function that displays n is a number only if is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """Function that displays a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Function that displays whether n is odd or even"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
