#!/usr/bin/python3
""" starts a Flask web application."""

from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """returns a rendered html template at /state_list route"""
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """returns a rendered html template at /state_list by id route"""
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
        return render_template('9-states.html')


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
