#!/usr/bin/python3
"""
This module defines a Flask application with four routes:
- '/'
- '/hbnb'
- '/c/<text>'
- '/python/' (default value of 'text' is 'is cool')
- '/python/<text>'
It also includes two additional routes for testing:
- '/number/<int:n>'
- '/number_template/<int:n>'

Each route returns a string or renders a template, based on the input.


To test the '/python/<text>' route with an input value of 'test':
- Start the application with the above command
- Open a web browser and go to: http://localhost:5000/python/test
- The page should display the string: "Python test"
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns a greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns the acronym 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Returns the string 'C ' followed by the value of the <text> variable,
    with underscores replaced by spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Returns the string 'Python ' followed by the value of the <text> variable,
    with underscores replaced by spaces. If no value is provided for <text>,
    the default value is 'is cool'.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Returns the value of the <n> variable followed by the string 'is a number'.
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders a template called 'number.html', passing the value of the <n> variable
    to the template as a context variable.
    """
    return render_template('number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

