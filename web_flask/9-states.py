#!/usr/bin/python3
"""Import Modules"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Function to close the connection to the database"""
    storage.close()


@app.route("/states/", defaults={"id": None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_states(id):
    """Displays states and cities"""
    states = storage.all(State).values()
    if id:
        state_by_id = None
        for state in states:
            if state.id == id:
                state_by_id = state
        return render_template("9-states.html", state=state_by_id, id=id)
    else:
        return render_template("9-states.html", states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
