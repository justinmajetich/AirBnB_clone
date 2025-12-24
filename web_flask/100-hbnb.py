#!/usr/bin/python3
"""HBNB is alive"""

from models import storage, State, Amenity, Place, User
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Fetch model data from storage engine"""

    states_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    place_dict = storage.all(Place)

    return render_template(
        '100-hbnb.html',
        states_dict=states_dict,
        amenities=amenity_dict,
        places=place_dict
    )


@app.teardown_appcontext
def teardown_appctxt(exception):
    """Close database session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
