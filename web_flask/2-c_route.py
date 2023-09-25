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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
