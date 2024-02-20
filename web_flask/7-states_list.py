#!/usr/bin/python3
""" Starts a new Flask web application. """

from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns the text Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """" Returns the text HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Returns “C ” followed by the value of the text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is_cool'):
    """" Returns “Python”, followed by the value of the text variable. """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Returns “n is a number” only if n is an integer. """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """ Returns a HTML page only if n is an integer. """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_or_even(n):
    """ Returns “Number: n is even|odd” inside the tag BODY. """
    return render_template('6-number_odd_or_even.html', number=n,
                           odd_even=('odd' if n % 2 != 0 else 'even'))


@app.route('/states_list')
def states_list():
    """ Returns states. """
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
