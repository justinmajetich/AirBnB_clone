#!/usr/bin/python3

"""This is the module documentation"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
"""
Script that starts a Flask
Web app for my HBNB clone project
"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C " + f'{text}'.replace("_", " ")


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    if text == "is cool":
        return "Python is cool"
    else:
        return "Python " + f'{text}'.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


@app.route("/states_list", strict_slashes=False)
def state_list():
    all_states = storage.all(State).values()
    return render_template('7-states_list.html',
                           all_states=all_states, header="States")


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', all_states=all_states,
                           header="States")


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
