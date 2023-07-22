#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, escape, Markup
from models import *
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters_route():
    '''Retrieves States, Cities and Amenities for HTML rendering'''
    all_states = storage.all('State').values()
    all_amenities = storage.all('Amenity').values()
    all_places = storage.all('Place').values()
    for place in all_places:
        place.description = Markup(place.description.replace('\n', '<br />'))

    return render_template('100-hbnb.html',
                           states=all_states,
                           amenities=all_amenities,
                           places=all_places)


@app.teardown_appcontext
def close_session(exception):
    """Closes the database session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
