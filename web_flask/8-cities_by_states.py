#!/usr/bin/python3
"""Script to start a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a list of states and their associated cities."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    cities_dict = {}
    for state in sorted_states:
        if state.cities:
            sorted_cities = sorted(state.cities, key=lambda x: x.name)
            cities_dict[state.id] = sorted_cities
    return render_template(
        '8-cities_by_states.html',
        states=sorted_states,
        cities=cities_dict)


@app.teardown_appcontext
def teardown(exception):
    """Close the storage engine session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
