#!/usr/bin/python3
"""HBNB"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def closeConnection(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def printState():
    """printState"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """Initial"""
    app.run(host='0.0.0.0', port=5000)
