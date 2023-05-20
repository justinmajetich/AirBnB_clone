#!/usr/bin/python3
""" A script that displays a list of states and City objects
    linked to the State
"""
from flask import Flask, render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display an HTML page with list of states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, route='states')


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display an HTML page with list of City objects linked to the State"""
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            return render_template('9-states.html', id=id, states=states,
                                   route='id')
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_app_context(exception):
    """It removes the current SQLAlchemy sessions after each requests"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
