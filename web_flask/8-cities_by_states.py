#!/usr/bin/python3
"""Starts a Flask web app"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """returns a rendered html template at /cities_by_state route"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    """Removes SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
