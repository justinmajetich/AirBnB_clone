#!/usr/bin/python3
"""
Importing the flask module
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def stateList():
    """A function that displays the list of states from
    the storage eather the fs or db."""
    return render_template("7-states_list.html",
                           statesStorage=storage.all(State))


@app.route("/states_list", strict_slashes=False)
def teardown_appcontext():
    """A function that removes the session after each reuest."""
    storage.close()


if __name__ == "__main__":
    app.run()
