#!/usr/bin/python3
""" Script that runs a Flask app """
from flask import Flask, escape
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
