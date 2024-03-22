#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route /
    Displays: 'Hello HBNB'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route /hbnb
    Displays: 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    Route /c/<text>
    Displays: 'C ' followed by the value of the 'text' variable and replaces
    underscore '_' symbol with a space ' '
    """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Route /python/<text>
    Displays: 'Python ' followed by the value of the 'text' variable and
    replaces underscore '_' symbol with a space ' '. The default values
    of 'text' is 'is cool'
    """
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route /number/<n>
    Displays: 'n is a number' only if 'n' is  an integer
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route /number_template/<n>
    Displays: HTML page only if 'n' is  an integer
        - 'H1' tag: 'Number: n' inside the tag 'BODY'
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
