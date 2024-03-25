#!/usr/bin/python3
"""Simple Flask Module instance"""
from flask import Flask, render_template

from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a HTML page with all State, City, Amenity objects in Storage"""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    cities = storage.all(City)
    cities = sorted(cities.values(), key=lambda city: city.name)
    amenities = storage.all(Amenity)
    amenities = sorted(amenities.values(), key=lambda amenity: amenity.name)
    places = storage.all(Place)
    places = sorted(places.values(), key=lambda place: place.name)
    return render_template(
        "100-hbnb.html", states=states, cities=cities, amenities=amenities, places=places
    )


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
