#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import render_template, Flask
app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """hbnb filters"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(stuff):
    """Remove current SQLAlchemy sesh"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
