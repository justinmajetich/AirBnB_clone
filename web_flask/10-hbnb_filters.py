#!/usr/bin/python3
"""HBNB filters"""

from models import storage, State, Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Fetch states and cities in relation to amenities"""

    states_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    return render_template(
        '10-hbnb_filters.html',
        states_dict=states_dict,
        amenities=amenity_dict
    )


@app.teardown_appcontext
def teardown_appctxt(exception):
    """Close database session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
