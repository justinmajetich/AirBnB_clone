#!/usr/bin/python3
"""
This module defines a Flask web application that displays a list of all State
objects present in the database.
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """
    Renders an HTML page with a list of
    all State objects present in the database.
    """
    states = storage.all("State").values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_sorted)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
