#!/usr/bin/python3
"""Starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """closes the current SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """displays the list1 of states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", states=state, id=state.id)
    return render_template("9-states.html", states=state, id='none')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
