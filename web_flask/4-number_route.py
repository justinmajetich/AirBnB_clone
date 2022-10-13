#!/usr/bin/python3
'''
Start a Flask web application
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    site index
    '''
    return 'Hello HBNB!'


@app.route('/hbnb/', strict_slashes=False)
def hbnb():
    '''
    hbnb page
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    c is fun!
    '''
    return ' '.join(['C', text.replace('_', ' ')])


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    '''
    python is cool!
    '''
    return ' '.join(['Python', text.replace('_', ' ')])


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    '''
    n is a number
    '''
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
