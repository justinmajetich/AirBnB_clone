#!/usr/bin/python3
"""
This script serves multiple URLs with given variables
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Handles requests to root URL

    Returns:
        str: greeting string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handles requests to HBNB

    Returns:
        str: HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Return a string that starts with "C " and is followed by
    the value of the text variable.

    Args:
        text (str): The text to include in the returned string.

    Returns:
        str: C with given text
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Return python plus string stored in variable text

    Args:
        text (str): "is cool"

    Returns:
        str: Python is cool
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    """
    Displays 'n is a number' only if n is an integer

    Args:
        n (int): number

    Returns:
        str: n 'is a number' if n is a number
    """
    return "{}is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    """Start development server"""
    app.run(host='0.0.0.0', port=5000)
