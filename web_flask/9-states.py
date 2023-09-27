#!/usr/bin/python3
"""Script to start a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """Display a list of states."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """Display cities of a specific state."""
    state = storage.get(State, state_id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    """Close the storage engine session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
