#!/usr/bin/python3
""" This script starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of states and their cities.

    The list is sorted by state name and cities are sorted by name.

    Returns:
        str: HTML content to be displayed.
    """
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states_list)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
