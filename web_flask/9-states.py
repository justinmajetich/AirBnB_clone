#!/usr/bin/python3
"""
starts a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def citystates():
    ''' Display page with list of all states and related cities '''
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    ''' reset the session of db storage '''
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
