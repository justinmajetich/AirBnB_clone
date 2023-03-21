#!/usr/bin/python3
"""
This module defines a Flask application with four routes:
- '/'
- '/hbnb'
- '/c/<text>'
- '/python/' (default value of 'text' is 'is cool')
- '/python/<text>'
- '/number/<int:n>'
- '/number_template/<int:n>'

Each route returns a string or renders a template based on the input text or integer.

To run the application, use the following command:
python3 -m flask run --host=0.0.0.0 --port=5000
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Returns a greeting string.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB' string.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Returns a string with 'C' followed by the input text with underscores replaced by spaces.
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Returns a string with 'Python' followed by the input text with underscores replaced by spaces.
    If no input text is provided, returns the string 'Python is cool'.
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Returns a string with the input number followed by the text 'is a number'.
    """
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML template with the input number displayed on the page.
    """
    return render_template('number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
