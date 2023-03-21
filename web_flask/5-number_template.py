#!/usr/bin/python3
"""
This script defines a Flask application with five routes:
- '/'
- '/hbnb'
- '/c/<text>'
- '/python/' (default value of 'text' is 'is cool')
- '/python/<text>'
- '/number/<int:n>'
- '/number_template/<int:n>'

The routes return various strings and HTML templates based on the input text or number.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Displays 'Hello HBNB!' when the '/' route is requested.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when the '/hbnb' route is requested.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Displays 'C ' followed by the input text with underscores replaced by spaces
    when the '/c/<text>' route is requested.
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Displays 'Python ' followed by the input text with underscores replaced by spaces
    when the '/python/' or '/python/<text>' route is requested. The default value
    of 'text' is 'is cool' if no text is provided.
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays '<n> is a number' when the '/number/<int:n>' route is requested,
    where <n> is the input integer.
    """
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders the '5-number.html' template and passes the input integer to it
    as a variable named 'n' when the '/number_template/<int:n>' route is requested.
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
