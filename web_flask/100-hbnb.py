#!/usr/bin/python3
"""Script to start a Flask web application for HBNB."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)

# Define a method to remove the current SQLAlchemy session after each request.


@app.teardown_appcontext
def teardown(exception):
    """Close the storage engine session."""
    storage.close()

# Define a route for /hbnb


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display an HTML page similar to 8-index.html."""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)

    return render_template('100-hbnb.html', states=states, cities=cities,
                           amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
