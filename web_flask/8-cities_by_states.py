#!/usr/bin/python3
"""Lists cities and states."""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database again at the end of the request."""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    """Handles the state route"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
