#!/usr/bin/python3
'''
3-python_route module
'''

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C %s' % escape(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    return 'Python %s' % escape(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
