#!/usr/bin/python3
"""
This module starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """
    Displays all the State objects in a list.
    """
    allstates = storage.all(State)
    this_state = None
    if id:
        this_state = allstates.get('State.{}'.format(id))
        allstates = None
    return render_template('9-states.html', allstates=allstates,
                           this_state=this_state)


@app.teardown_appcontext
def teardown(done):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
