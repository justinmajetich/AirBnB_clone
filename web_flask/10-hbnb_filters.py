#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Filters the current request
    """
    data = {
        "states": storage.all("State").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("10-hbnb_filters.html", models=data)


@app.teardown_appcontext
def tear(exception=None):
    """
    Ensures that all the states are closed before returning to the database
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
