#!/usr/bin/python3
"""Script that starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
    /hbnb_filters: display HTML page the shows a filter
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays an HTML page with a filter of States and Amenities

    All are sorted by name
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return (render_template('10-hbnb_filters.html',
    states=states, amenities=amenities))


@app.teardown_appcontext
def close_current_session(exception):
    """Close the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
