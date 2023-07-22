#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_route(state_id=None):
    """Displays a HTML page with the states and their cities
        listed in alphabetical order"""
    states = storage.all("State").values()
    the_state = storage.all('State').get('State.' + str(state_id), None)
    return render_template('9-states.html',
                           states=states,
                           a_state=the_state,
                           state_id=state_id)


@app.teardown_appcontext
def close_session(exception):
    """Closes the database session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
