#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_HNNB():
    """return HBNB"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def hello_txt(text):
    """return the text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_txt(text='is cool'):
    """return HBNB"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def python_number(n):
    """Retrun the number"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def python_number_template(n=None):
    """Retrun the number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def python_number_odd_or_even_template(n=None):
    """Retrun the number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
