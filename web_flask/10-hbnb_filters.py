#!/usr/bin/python3
"""
Module with Script that starts the 
HBNB clone flask web application

"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
"""
Script that starts a Flask
Web app for my HBNB clone project

"""
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def displayHBNB():
    """
    Renders the HTML of HBNB clone project,
    with database information included
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
