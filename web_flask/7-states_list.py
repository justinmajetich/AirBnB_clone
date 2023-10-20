#!/usr/bin/python3
"""
This module list all the states in the database
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This method load cities in a state from the storage"""
    states = list(storage.all(State).values())
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(execute):
    """This method close the SQLAlchemy session"""
    return storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
