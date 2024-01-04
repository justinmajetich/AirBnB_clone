#!/usr/bin/python3
""" This module starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page like 6-index.html with filters loaded from DBStorage.

    The filters include states and amenities, sorted by name.

    Returns:
        str: HTML content to be displayed.
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template(
        '10-hbnb_filters.html',
        states=sorted(states.values(), key=lambda state: state.name),
        amenities=sorted(amenities.values(), key=lambda amenity: amenity.name)
    )


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
