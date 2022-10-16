#!/usr/bin/python3
'''
    a python script that a flask web application
'''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_word():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def c_is_python(text="is cool"):
    return ('Python %s' % text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return ('%d is a number' % n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even', strict_slashes=False)
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
