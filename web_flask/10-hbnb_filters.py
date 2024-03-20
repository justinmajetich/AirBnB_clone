#!/usr/bin/python3
"""Flask module for search engine"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Closes session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays a list of states and amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
