#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import State
from models import Amenity
from models import Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display an HTML page like 8-index.html, done during the
        0x01. AirBnB clone - Web static project
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_app_context(exception):
    """It removes the current SQLAlchemy sessions after each requests"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
