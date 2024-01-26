#!/usr/bin/python3
"""list the states of my database"""


from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a list of states and render it as an HTML template."""

    States = storage.all(State)

    return render_template("8-cities_by_states.html", states=States)


@app.teardown_appcontext
def tear_db(exception):
    """Teardown function to close the database connection."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
