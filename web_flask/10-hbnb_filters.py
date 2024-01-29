#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filter():
    # Get states and amenities from the storage
    states = storage.all(State)
    amenities = storage.all(Amenity)

    # Rendering the template
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def tear_db(e):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
