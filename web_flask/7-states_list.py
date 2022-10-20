#!/usr/bin/python3
"""This module starts Flask web application and uses storage for fetching data from the storage engine"""


from models import *
from flask import Flask, render_template


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

@app.route('/c/<string:text>')
def hello_text(text):
    """Return C followed by a variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/')
@app.route('/python/<string:text>')
def hello_python(text='is cool'):
    """Return python and a variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def hello_num(n):
    """Return an int n"""
    n = str(n)
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def hello_template(n):
    """Return an html template"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def hello_odd_even(n):
    """Return an html template and n"""
    return render_template('6-number_odd_or_even.html', n=n)

@app.route('/states_list')
def state_list():
    """Return the list of state in an html template"""
    return render_template('7-states_list.html', states=storage.all('State'))

@app.teardown_appcontext
def teardown(err):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
