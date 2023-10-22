#!/usr/bin/python3
"""This is a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """To print all the cities in the database"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Print states if with id"""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template("9-states.html", state=state, cities=cities)
    return render_template("9-states.html")


@app.teardown_appcontext
def close_session(ctx):
    """To remove the current SQL Alchemy"""
    storage.close()


if __name__ == '__main__':
    # app.run(Debug=True)
    app.run(host="0.0.0.0", port=5000)
