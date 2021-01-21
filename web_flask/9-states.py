#!/usr/bin/python3
"""Start Flask application"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """ displays a state with specified id  """
    states = storage.all('State')
    if id:
        key = 'State.' + id
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = states.values()
    return render_template('9-states.html', states=states,
                           id=id)


@app.teardown_appcontext
def teardown(self):
    """Remove session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
