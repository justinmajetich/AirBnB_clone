#!/usr/bin/python3
"""
Script that starts a Flask web application. 
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Adding a specific route /hbnb"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text=None):
    """Dynamic inputed text: C + replace _ for space and show text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is cool'):
    """Dynamic inputed text: Python + replace _ for space and show text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def only_digits_dynamic(n=None):
    """Dynamic inputted integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
