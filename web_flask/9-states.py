#!/usr/bin/python3
"""Start a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with list of all State objects"""
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display a HTML page with cities of a specific State"""
    state = None
    states = storage.all('State').values()
    for st in states:
        if st.id == id:
            state = st
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
