#!/usr/bin/python3
"""Define ``7-states_list`` module. Import Flask
   class and create a new class instance called ``app``.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask('web_flask')


@app.route('/states_list', strict_slashes=False)
def list_states():
    """Display HTML page containg a list of states"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def close_db_session(exc):
    """Remove/close the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
