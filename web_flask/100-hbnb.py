#!/usr/bin/python
"""Contains the /hbnb route."""
from flask import Flask, render_template

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """Close the database at the end of the request."""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb(id=None):
    """HBNB route."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    print(amenities)
    cities = storage.all(City)
    places = storage.all(Place)
    return render_template(
        "100-hbnb.html",
        states=states.values(),
        amenities=amenities.values(),
        cities=cities.values(),
        places=places.values()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
