#!/usr/bin/python3
"""Starts a Flask web application.
Listening on 0.0.0.0 port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all(State)
    states_list = []
    for state_id, state in states.items():
        states_list.append((state.name, state.id))
    states_list.sort()
    return render_template('7-states_list.html', states_list=states_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
