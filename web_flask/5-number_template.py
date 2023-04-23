#!/usr/bin/python3
""" This script start at any ip address of 0.0.0.0 in port 5000 """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ This function simply renders the string 'Hello HBNB' """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Rendering a string 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Rendering a variable and replacing '_' with space """
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    apt.run(host='0.0.0.0', port=5000)
