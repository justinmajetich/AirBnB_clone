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


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_states(id=None):
    """Handles the state route"""
    states = storage.all(State)
    if id is not None:
        state = states.get("State.{}".format(id))
        if state is None:
            states = None
        else:
            states = [state]
    else:
        states = states.values()
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
