#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function to return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ function to display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """ function to display C + value of text """
    text = text.replace("_", " ")
    return 'C {}'.format(escape(text))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
