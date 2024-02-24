#!/usr/bin/python3
"""
    python script that starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask, render_template, request, jsonify
from os import getenv


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return: HTML page with list of states"""
    path = '7-states_list.html'
    states = storage.all(State)
    """sort State object alphabetically by name"""
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """ Clean-up session"""
    storage.close()


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
