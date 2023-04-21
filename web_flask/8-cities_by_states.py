#!/usr/bin/python3
"""
This module starts a Flask web application
that listens on 0.0.0.0, port 5000 and
displays a list of cities by state
from the AirBnB_clone_v2 database.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with a list of states and their associated cities
    from the AirBnB_clone_v2 database.
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
