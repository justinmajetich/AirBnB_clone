#!/usr/bin/python3
"""starts a Flask web application"""
from models import Storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_1(id=None):
    """Returns a rendered html template:
    if id is given, list the cities of that State
    else, list all States
    """
    states = storage.all('State')
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all('State').values()
    return render_template('9-states.html', states=states


@app.teardown_appcontext
def teardown():
    """ removes currents SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
