#!/usr/bin/python3
""" This script starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Hello hbnb """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ C text """
    text_with_spaces = text.replace('_', ' ')
    return 'C {}'.format(text_with_spaces)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
