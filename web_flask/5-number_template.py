#!/usr/bin/python3
"""
/number/<n>: display “n is a number” only if n is an integer
using render template to render the html
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<c_variable>', strict_slashes=False)
def cisfun(c_variable):
    return 'C {}'.format(c_variable.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/p/<python_variable>', strict_slashes=False)
def pythoniscool(python_variable='is_cool'):
    return 'Python {}'.format(python_variable.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
