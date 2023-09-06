#!/usr/bin/python3
"""Script that have 7 routes"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    "return Hello hbnb"
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """replace _ with spaces"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """python route"""
    if text is not "is cool":
        text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """Route that print if n is integer"""
    if type(n) is int:
        return f"{n} is a number"
    else:
        raise TypeError


@app.route('/number_templates/<int:n>', strict_slashes=False)
def html_page(n):
    """route to display a html"""
    if type(n) is int:
        return render_template('5-number.html', number=n)
    else:
        raise TypeError


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    """route that evaluates if n is odd or even"""
    if type(n) is int:
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html',
                                   number=n, text='even')
        else:
            return render_template('6-number_odd_or_even.html',
                                   number=n, text='odd')
    else:
        raise TypeError


@app.route('/states_list', strict_slashes=False)
def state_list():
    """function that print every state on the html"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """function that close the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
