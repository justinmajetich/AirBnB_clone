#!/usr/bin/python3

"""Script that starts a Flask web apllication"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """loads all cities of a State"""

    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """closes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
