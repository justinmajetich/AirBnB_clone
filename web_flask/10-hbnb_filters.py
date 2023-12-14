#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import environ

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(self):
    """
    Teardown method for app context
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display HTML page with filters
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()

    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
