#!/usr/bin/python3
""" This script starts a web flask application"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Displays C followed by text variable"""
    return "C " + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Displays Python followed by text variable"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    """Displays n is a number only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays HTML page with the value of n"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    