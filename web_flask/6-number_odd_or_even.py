#!/usr/bin/python3
"""
a script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ A function that display Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """" A function that display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ a function that recieves a keyword argument and display a message """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': "is_cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ A function that recives a keyword argument and display a message """
    return 'python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num_n(n):
    """ A function that n is a number only if n is an integer """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ a function that receives a number and render a message """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_even_odd(n):
    """ a function that receives a number argument, and render """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
