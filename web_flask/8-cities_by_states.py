#!/usr/bin/python3
"""Define ``8-cities_by_states`` module. Import Flask
   class and create a new class instance called ``app``.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask('web_flask')


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display an HTML page containg a list of states and
       a list of cities under them.
    """
    all_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def close_db_session(exc):
    """Remove/close the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
