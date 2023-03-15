#!/usr/bin/python3
from flask import Flask, render_template
"""
intializing flask web app
"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Display "Hello HBNB!"
    """
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """
    route /hbnb displays
    """
    return ('HBNB')


@app.route('/c/<text>')
def c(text):
    """
    replaces _ with spaces
    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def py(text="is cool"):
    """
    default adds is cool and replaces _ with space
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>')
def num(n):
    """
    displays only if the added is an int
    """
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>')
def template(n):
    """
    routes /number_templates with n integer
    """
    return (render_template('5-number.html', n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
