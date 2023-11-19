#!/usr/bin/python3
"""
This module list all the states in the database
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """This method load cities in a state from the storage"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(execute):
    """This method close the SQLAlchemy session"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
