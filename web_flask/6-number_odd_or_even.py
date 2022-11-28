#!/usr/bin/python3
"""
Task 1 for Flask Project Web Framework
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Returns Hello HBNB for the '/' url
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Returns HBNB for the /hbnb route
    """
    return "HBNB"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_magic(text='is cool'):
    """
    Display Python, followed by the value of the text
    replace underscore _ symbols with a space
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        result = "{} is even".format(n)
        return render_template('6-number_odd_or_even.html', result=result)
    result = "{} is odd".format(n)
    return render_template('6-number_odd_or_even.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
