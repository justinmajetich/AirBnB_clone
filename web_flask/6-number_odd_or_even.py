#!/usr/bin/python3
"""
Runs a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ display “C ” followed by the value of the text variable """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonisfun(text="is cool"):
    """ display “Python ”, followed by the value of the text variable """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def iamanumber(n):
    """ display “n is a number” only if n is an integer """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberandtemplates(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    display a HTML page only if n is an integer
    and determine whether it is odd or even
    """
    if (n % 2 == 0):
        evenness = "even"
    else:
        evenness = "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness_disp=evenness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
