#!/usr/bin/python3
"""a script that starts a Flask web application and display a HTML page"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    """Return a string"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello():
    """Return a string"""
    return 'HBNB'

@app.route('/c/<text>')
def hello_c(text):
    """Return string and a variable text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/')
@app.route('/python/<text>')
def hello_python(text='is cool'):
    """Return a string and a variable text"""
    text = text.replace('_', ' ')
    return 'Pythin {}'.format(text)

@app.route('/number/<int:n>')
def number(n):
    """Return an integer n"""
    n = str(n)
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def num_template(n):
    """Return an integer n"""
    n = str(n)
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    