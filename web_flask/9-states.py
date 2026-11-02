#!/usr/bin/python3
"""Starts a flask app
    listens to 0.0.0.0:5000
"""
from flask import Flask, render_template
from models.__init__ import storage
from flask import Flask

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state():
    """"displays an HTML page with a list of all in related cities.
    sorted by name an id
    """
    state = storage.all('State')
    return render_template('9-states.html', state=state)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """removes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
