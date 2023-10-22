#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """
    cities_by_states: display a HTML page
    """
    states = storage.all("State").values()
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def stet(id):
    """
    stet
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)


@app.teardown_appcontext
def tear(exception=None):
    """
    Ensures that all the states are closed before returning to the database
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
