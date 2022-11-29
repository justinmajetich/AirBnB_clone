#!/usr/bin/python3
"""Starts a Flask web application"""
from models.state import State
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """closes the current SQLAlchemy session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """displays the list1 of states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
