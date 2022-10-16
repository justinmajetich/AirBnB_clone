#!/usr/bin/python3
"""starts a Flask web application"""
from models import Storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Returns a rendered html template,
    using the web_static files
    """
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', **locals())


@app.teardown_appcontext
def teardown():
    """ removes currents SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
