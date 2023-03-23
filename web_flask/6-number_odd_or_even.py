#!/usr/bin/python3

""" This script writes a script that starts a Flask web application listening 
at port 0.0.0, port 50

"""

from Flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)