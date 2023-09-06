#!/usr/bin/python3
"""Script that start a Flask webapp"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hell():
    """function to return a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """prints hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """"replace _ with spaces"""
    text = text.replace('_', ' ')
    return f"c {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    """print is cool"""
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """"print if is int"""
    if type(n) is int:
        return f"{n} is a number"
    else:
        raise TypeError


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_page(n):
    """print html"""
    if type(n) is int:
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    """route that evaluates if n is odd or even"""
    if type(n) is int:
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html', number=n, text='odd')
    else:
        raise TypeError


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
