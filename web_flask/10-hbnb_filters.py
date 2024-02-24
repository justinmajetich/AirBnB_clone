#!/usr/bin/python3
""" A flask script that returns state object's id and name
"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State
import os

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ remove the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ display a HTML page """
    # return a list of State object.
    states = list(storage.all(State).values())
    # sort by name with case insensitive
    states = sorted(states, key=lambda state: state.name.lower())

    amenities = list(storage.all(Amenity).values())
    states_dict = {}
    for state in states:
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            states_dict[state] = sorted(
                state.cities, key=lambda city: city.name)
        else:
            states_dict[state] = sorted(
                state.cities(), key=lambda city: city.name.lower())

    return render_template('10-hbnb_filters.html',
                           states=states_dict, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
