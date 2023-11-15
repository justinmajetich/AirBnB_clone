#!/usr/bin/python3
"""Script that starts a flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    c_text = text.replace('_', ' ')
    return f'C {c_text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    python_text = text.replace('_', ' ')
    return f'Python {python_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_or_even(n):
    if n % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    return render_template('6-number_odd_or_even.html', number=n,
                           num_odd_or_even=num_odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
