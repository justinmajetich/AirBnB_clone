#!/usr/bin/python3
"""10-hbnb_filters module
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State, Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def states():
    """Displays HTML page like 6-index.html"""
    return render_template("10-hbnb_filters.html",
                           location=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())


@app.teardown_appcontext
def storage_close(var=None):
    """Removes current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
