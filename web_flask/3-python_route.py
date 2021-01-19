#!/usr/bin/python3
"""[HBNB]"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def anyText(text):
    """def anyText"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def anyTextWithPython(text='is cool'):
    """def anyText with python"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

if __name__ == '__main__':
    """Main"""
    app.run(host='0.0.0.0', port=5000)
