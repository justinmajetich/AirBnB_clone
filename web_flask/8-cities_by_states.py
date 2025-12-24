#!/usr/bin/python3
"""List cities by states"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """Fetch states from storage engine"""
    storage_dict = storage.all(State)
    return render_template('8-cities_by_states.html', states=storage_dict)


@app.teardown_appcontext
def teardown_appctx(exception):
    """Remove DB session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
