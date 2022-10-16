#!/usr/bin/python3
""" Script that runs a Flask app """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def closing(error):
    """closes session """
    storage.close()


@app.route('/states/', strict_slashes=False)
def states():
    """ function that list states"""
    state = storage.all('State')
    return render_template('9-states.html', state=state)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ function that list a state by id"""
    state = storage.all('State')
    return render_template('9-states.html', state=state, id=id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
