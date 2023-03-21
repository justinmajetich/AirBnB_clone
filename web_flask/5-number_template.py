#!/usr/bin/python3

"""
This is a Flask application that defines several routes.

Routes:
- /: returns a greeting message
- /hbnb: returns the message "HBNB"
- /c/<text>: returns the message "C <text>", replacing underscores with spaces
- /python: returns the message "Python is cool" by default, or "Python <text>"
  if a value for <text> is provided
- /number/<int:n>: returns the message "<n> is a number"
- /number_template/<int:n>: renders a Jinja2 template that displays the message
  "<n> is a number"
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
