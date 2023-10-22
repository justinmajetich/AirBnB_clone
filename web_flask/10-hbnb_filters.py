#!/usr/bin/python3
"""This is a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """To show html page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def close_session(ctx):
    """To remove the current SQL Alchemy"""
    storage.close()


if __name__ == '__main__':
    # app.run(Debug=True)
    app.run(host="0.0.0.0", port=5000)
