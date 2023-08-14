#!/usr/bin/python3
"""Import Modules"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Main Route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb Route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c route , return text with spaces"""
    text_with_spaces = text.replace('_', ' ')
    return f"C {text_with_spaces}"


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """python route, return text with spaces"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """number route, return if only is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    """return"""
    return render_template("5-number.html", n=n)


"""Entry Point"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
