#!/usr/bin/python3
"""
Displays the states lists
"""

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('10-hbnb_filters.html')

@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    """Lists all the states with the storage.all() method"""
    from models import storage
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exit):
    """Closes the database when the session ends"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
