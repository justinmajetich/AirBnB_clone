#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Displays 'C ' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """Displays 'Python ' followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Displays 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
