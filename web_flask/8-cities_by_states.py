#!/usr/bin/python3
""" Starting a Flask web application """

from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ html page including a list of states 
    and related cities as well"""
    states = storage.all("states")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(execpt):
    """ removin gthe SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)