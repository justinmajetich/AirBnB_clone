#!/usr/bin/python3
'''
Module Docs
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Method Docs'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Method Docs'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Method Docs'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    '''Method Docs'''
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Method Docs'''
    return f"{n:d} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Method Docs'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''Method Docs'''
    if n % 2 == 0:
        num_type = 'even'
    else:
        num_type = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, num_type=num_type)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
