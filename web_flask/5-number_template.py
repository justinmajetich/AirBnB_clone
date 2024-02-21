#!/usr/bin/python3
"""a script that starts a flask web"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """initials the url"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """texts"""
    return 'C ' + escape(text).replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """text"""
    return 'Python ' + escape(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """template"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)
    else:
        return 'Not Found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
