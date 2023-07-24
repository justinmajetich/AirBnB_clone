#!/usr/bin/python3
""" Script that starts a Flask web app on :500 """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hi_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):

    # Replace _ with a space
    rep_text = text.replace('_', ' ')
    return ("C {}".format(rep_text))


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):

    # Replace _ with a space
    rep_text = text.replace('_', ' ')
    return ("Python {}".format(rep_text))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):

    # Verify if number is even or odd
    if n % 2 == 0:
        type = "even"
    else:
        type = "odd"

    return render_template('5-number.html', n=n, type=type)


if __name__ == '__main__':
    app.run()
