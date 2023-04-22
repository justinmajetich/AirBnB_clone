#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays a string at /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of the text variable"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays 'Python', followed by the value of the text variable"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays Number: n is even|odd” inside the tag BODY"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
