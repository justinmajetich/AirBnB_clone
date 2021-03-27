#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Displays hello message
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Displays the name
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text):
    """
        Displays C with custom text
    """
    return "C %s" % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>/', strict_slashes=False)
def pythonroute(text='is_cool'):
    """
        Displays Python with custom text
    """
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        Displays number if it is of type int
    """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
        Renders number template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
        Renders number template that displays if odd or even
    """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def get_states_list():
    """
        Returns a states list-infused template
    """
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
