#!/usr/bin/python3
"""placeholder"""
from flask import render_template, Flask

app = Flask(__name__)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_mod_two(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def num_int(n):
    return "{} is a number".format(n)


@app.route('/', methods=['GET'], strict_slashes=False)
def holla_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnbbb():
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c_is_meh(text):
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'},
           methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python_awesome(text):
    return "Python " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
