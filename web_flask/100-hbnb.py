#!/usr/bin/python3
# File: 100-hbnb.py
# Authors: Yoshua Lopez - Ma Paz Quirola - Laura Socarras 

""""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:
            /hbnb_filters:        Display a HTML page like 8-index.html
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """After each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters')
def states_and_cities():
    """Display html page w/ working city/state filters & amenities/proper
       Runs with web static css files
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    dict = {"states": states, "amenities": amenities, "places": places}
    return(render_template("100-hbnb.html", **dict))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
