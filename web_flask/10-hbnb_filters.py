#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import *
from models import storage
from models import state
from models import amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filter():
    # Get states and amenities from the storage
    states = storage.all(state)
    amenities = storage.all(amenity)

    # Rendering the template
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def tear_db(e):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
