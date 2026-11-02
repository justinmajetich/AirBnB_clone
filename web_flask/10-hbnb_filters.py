#!/usr/bin/python3
"""A flask application"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """method closes a current db session"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """displays html page with state and city filters"""
    state_obj = [state for state in storage.all("State").values()]
    amenity_obj = [amenity for amenity in storage.all("Amenity").values()]
    return render_template(
            '10-hbnb_filters.html', state_obj=state_obj,
            amenity_obj=amenity_obj)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
