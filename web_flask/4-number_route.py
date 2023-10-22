#!/usr/bin/python3
"""Flask package"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """hello world testing"""
    return 'Hello HBNB!'


@app.route('/hbnb/', strict_slashes=False)
def disp_hbnb():
    """hello world testing"""
    return 'BNB'


@app.route('/c/<text>', strict_slashes=False)
def disp_var(text):
    """Variables testng"""
    return 'C %s' % escape(text).replace('_', ' ')


@app.route('/python/',
           strict_slashes=False,
           defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def disp_py_var(text):
    """Variables testng"""
    return 'Python %s' % escape(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def disp_num(n):
    """Number variables testng"""
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
