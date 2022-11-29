#!/usr/bin/python3
"""
Displays the states lists
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Lists all the states with the storage.all() method"""
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', states=state, id=state.id)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown(exit):
    """Closes the database when the session ends"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
