#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def show_state():
    """
    Displays an HTML page listing all `city`s inside
    of `state`, sorted by `name`.
    """
    return render_template('10-hbnb_filters.html', states=storage.all(State),
                           amenities=storage.all(Amenity))


@app.teardown_appcontext
def teardown(content):
    """
    Removes current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
