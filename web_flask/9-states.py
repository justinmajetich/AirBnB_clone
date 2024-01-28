#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display HTML page with list of states"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display HTML page with list of states and cities"""
    states = storage.all(State).values()
    statesSorted = sorted(states, key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=statesSorted)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ Route function for /states and /states/<id> """
    not_found = False

    if id is not None:
        states = storage.all(State, id)
        states_id = True
        if len(states) == 0:
            not_found = True
    else:
        states = storage.all(State)
        states_id = False

    return render_template('9-states.html', states=states,
                           states_id=states_id, not_found=not_found)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
