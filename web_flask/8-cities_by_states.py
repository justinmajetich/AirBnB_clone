#!/usr/bin/python3

"""Starts a Flask web application to display States and their Cities"""

from models import storage
from models.state import State
from flask import Flask, render_template, teardown_appcontext


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_states_cities():
    """ Display States and their Cities """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
