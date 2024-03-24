#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Called a function with / route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Called a function with /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function call with /c/<text> route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function call with /python/<text> route """
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function call with /number/<n> route """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function call with /number_template/<n> route """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
