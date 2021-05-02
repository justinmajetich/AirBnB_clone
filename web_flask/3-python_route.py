#!/usr/bin/python3
"""
scripts that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_replace(text):
    return "C " + text.replace("_", " ")


@app.route('/python/',strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/(<text>)', strict_slashes=False)
def python(text):
    return "Python" + text.repalce("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
