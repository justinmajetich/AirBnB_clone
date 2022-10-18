#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/hbnb_filters/', strict_slashes=False)
def display_html():
    """ Function called with /states route """
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html',
                           states=states.values(),
                           amenities=amenities.values())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
