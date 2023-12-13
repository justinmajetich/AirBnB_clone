#!/usr/bin/python3
""" This script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display filters in HTML page"""
    state = storage.all(State).values()
    amenity = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', state=state, amenity=amenity)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Function that removes the current SQL Alchemy Session after each
    request. """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
