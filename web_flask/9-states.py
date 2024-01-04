#!/usr/bin/python3
""" This module starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Display a HTML page with a list of states.

    The list is sorted by state name.

    Returns:
        str: HTML content to be displayed.
    """
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states_list)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """
    Display a HTML page with the cities of a given state.

    Args:
        id (str): The ID of the state.

    Returns:
        str: HTML content to be displayed.
    """
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
