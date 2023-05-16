#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """Render template with states
    """
    path = '10-hbnb_filters.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(path, states=states, amenities=amenities)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
