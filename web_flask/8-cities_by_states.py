#!/usr/bin/python3
"""cities by states"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Get list of states from db"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """Teardown method to close the db"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
