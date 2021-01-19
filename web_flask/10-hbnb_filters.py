#!/usr/bin/python3
"""HBNB"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def closeConnection(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def printState(id=None):
    """printState"""
    states = storage.all(State).values()
    if id is not None:
        id = 'state.' + id
    return render_template('9-states.html', states=states, id=id)

if __name__ == '__main__':
    """Initial"""
    app.run(host='0.0.0.0', port=5000)
