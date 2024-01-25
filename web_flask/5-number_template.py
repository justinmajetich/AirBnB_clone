#!/usr/bin/python3
"""flask projects"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting message"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns a string with 'C' followed by the value of 'text'"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Returns a string with 'python' followed by the value of 'text'"""
    text = text.replace("_", " ")
    return "python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns a string with the value of 'n' followed by 'is a number'"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Renders a template '5-number.html' with the value of 'n'"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
