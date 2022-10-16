#!/usr/bin/python3
""" Script that runs a Flask app """
from flask import Flask, escape, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ function that returns on url /"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ function that returns on url /hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def hello_c(text):
    """ function that returns a input"""
    return 'C %s' % escape(text.replace('_', ' '))


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<text>')
def hello_python(text):
    """ function that returns a input and has a default"""
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route("/number/<int:n>")
def number(n):
    """ function that returns a number"""
    return '%d is a number' % n


@app.route("/number_template/<int:n>")
def number_html(n):
    """ function that returns a number"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """ function that returns a number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
