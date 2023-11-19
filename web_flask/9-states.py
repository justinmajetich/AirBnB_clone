#!/usr/bin/python3
"""
This module list all the states in the database
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """This method load cities in a state from the storage"""
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route('/states/<id>', strict_slashes=False)
def city_list(id):
    """This method load cities in a state from the storage"""
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            cities = state.cities
            return render_template("9-states.html", state=state, cities=cities)

    return render_template("9-states.html")


@app.teardown_appcontext
def close_session(execute):
    """This method close the SQLAlchemy session"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
