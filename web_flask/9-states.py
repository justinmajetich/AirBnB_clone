#!/usr/bin/python3
"""7-states_list.py module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with a list of all states"""
    states = storage.all(State).values()
    if states is None:
        return render_template('9-states.html', states=None)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    '''Display a HTML page with a list of all states'''
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
