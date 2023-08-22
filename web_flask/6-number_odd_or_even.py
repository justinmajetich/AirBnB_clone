#!/usr/bin/python3
"""
This is a Flask web application with multiple routes and templates.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when accessing the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when accessing the '/hbnb' route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display "C " followed by the value of the text variable
    (replace underscores with spaces) when accessing the '/c/<text>' route.
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    """
    Display "Python " followed by the value of the text variable
    (replace underscores with spaces) when accessing the '/python/<text>' route
    The default value of text is "is cool".
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Display "<n> is a number" when accessing the
    '/number/<n>' route, only if n is an integer.
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display an HTML page with a header tag displaying
    "Number: n" when accessing the '/number_template/<n>' route
    only if n is an integer.
    """
    if isinstance(n, int):
        return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display an HTML page with a header tag displaying
    "Number: n is even|odd" when accessing the '/number_odd_or_even/<n>' route
    only if n is an integer.
    """
    if isinstance(n, int):
        even_or_odd = "odd" if n % 2 != 0 else "even"
        return render_template('6-number_odd_or_even.html', number=n, even_or_odd=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
