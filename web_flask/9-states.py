#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
import models
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Displays an HTML page with a list of states """
    states = models.storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Displays an HTML page with a list of states """
    states = models.storage.all(State)
    return render_template('9-states.html', states=states, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
