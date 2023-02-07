#!/usr/bin/python3
"""Flask Web App that returns list of states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown_db closes connections to database"""
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """get all state info from database"""
    state_dict = (storage.all(State)).values()
    return render_template("7-states_list.html", state_dict=state_dict)


@app.route("/cities_by_states", strict_slashes=False)
def city_list():
    """get all state and city info from database"""
    state_dict = (storage.all(State)).values()
    return render_template("8-cities_by_states.html", state_dict=state_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
