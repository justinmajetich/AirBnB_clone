#!/usr/bin/python3
"""Define ``9-state`` module. Import Flask
   class and create a new class instance called ``app``.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask('web_flask')


@app.route('/states', strict_slashes=False)
def states_route():
    """Display an HTML page containg a list of states and
       a list of cities under them.
    """
    all_states = storage.all(State)
    return render_template('9-states.html', page="states", states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def dynamic_city_route(id):
    """Display a state details page.

       Arguments:
         state_id: id of the state in the url
    """
    all_states = storage.all(State)
    for state in all_states.values():
        if id == state.id:
            return render_template('9-states.html',
                                   page="details",
                                   state=state)
    return render_template('9-states.html',
                           page="not found",
                           state=all_states)


@app.teardown_appcontext
def city(exc):
    """Remove/close the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
