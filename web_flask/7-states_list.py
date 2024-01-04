#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a HTML page with a list of states.

    The list is sorted by state name.

    Returns:
        str: HTML content to be displayed.
    """
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
