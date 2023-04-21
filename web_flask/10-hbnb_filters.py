#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnbfilters():
    """display the states and cities listed in alphabetical order"""
    cities = storage.all(City)
    states = storage.all(State)
    return render_template('10-hbnb_filters.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
