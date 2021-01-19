#!/usr/bin/python3
"""[HBNB]"""

from flask import Flask, escape

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


@app.route('/number/<int:number>', strict_slashes=False)
def isANumber(number):
    """Is a number"""
    return '{} is a number'.format(escape(number))


@app.route('/number_template/<int:number>', strict_slashes=False)
def number_template(number=None):
    """Number template"""
    return render_template('5-number.html', number=number)


if __name__ == '__main__':
    """Main"""
    app.run(host='0.0.0.0', port=5000)
