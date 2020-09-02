#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Print a str
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """
    Print a str
    """
    return 'HBNB'


@app.route('/c/<text>/', strict_slashes=False)
def is_fun(text):
    """
    Print a string, display “C ” followed by the value of
    the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def is_magic(text="is cool"):
    """
    Print a str, display “Python ”, followed by the
    value of the text variable
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Print a str, display “n is a number” only if n
    is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """
    Print a str, display “n is a number” only if n
    is an integer
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    Print a str, display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if n % 2:
        res = 'odd'
    else:
        res = 'even'
    return render_template('6-number_odd_or_even.html', number=n, odd_even=res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
