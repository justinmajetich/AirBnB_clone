#!/usr/bin/python3
"""states"""

from flask import Flask, render_template
from models.__init__ import storage
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
