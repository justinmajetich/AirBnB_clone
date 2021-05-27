#!/usr/bin/python3
"""
Intiatiate flask script application
display Integer
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
def p_cool():
    return "Python is cool"


@app.route('/python/<text>', strict_slashes=False)
def p_text(text):
    return ('Python %s' % text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def show_int(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
