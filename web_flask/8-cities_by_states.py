#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
import models


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a HTML page """
    states = storage.all(models.State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
