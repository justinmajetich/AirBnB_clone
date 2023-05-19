#!/usr/bin/python3
""" A script that starts a Flask web application:

    Add route:
        /python/(<text>): display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_is(text):
    """Display C followed by text"""
    replaced_text = text.replace('_', ' ')
    return 'C {}'.format(replaced_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def Python(text='is cool'):
    """Display python followed by text"""
    if text:
        replaced_text = text.replace('_', ' ')
        return 'Python {}'.format(replaced_text)
    else:
        return 'Python is cool'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
