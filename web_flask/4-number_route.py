#!/usr/bin/python3
""" a script that starts a Flask web application """


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays HELLO_HBNB"""
    return "HELLO_HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB in route /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ displays HBNB in route /hbnb """
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False, defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """ displays HBNB in route /hbnb """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ displays HBNB in route /number/n """
    return "{} is a number".format(n)


if __name__ == "__main__":
    """starts flask server """
    app.run(host='0.0.0.0', port=5000)
