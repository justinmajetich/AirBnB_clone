#!/usr/bin/python3
"""A script that starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# Define a teardown function to close the SQLAlchemy session after each
# request.


@app.teardown_appcontext
def close_storage_session(exception):
    """Teardown function to close the SQLAlchemy session."""
    storage.close()

# Define two routes for the application.


@app.route("/states/", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_states_and_cities(id=None):
    """Function called with routes '/states/' and '/states/<id>'."""

    # Fetch all states from the storage.
    all_states = storage.all(State)

    if not id:
        # Prepare a dictionary for rendering the list of states and their
        # names.
        states_dict = {state.id: state.name for state in all_states.values()}

        # Render the "7-states_list.html" template to display the list of
        # states.
        return render_template("7-states_list.html",
                               Table="States",
                               items=states_dict)

    # Prepare the key for the state with the provided ID.
    state_key = "State.{}".format(id)

    if state_key in all_states:
        # If the state is found, render the "9-states.html" template to display
        # the state's name and its associated cities.
        return render_template(
            "9-states.html",
            Table="State: {}".format(
                all_states[state_key].name),
            items=all_states[state_key])

    # If the state is not found, render the same template to display "Not
    # found!"
    return render_template("9-states.html", items=None)


if __name__ == "__main__":
    # Start the Flask application.
    app.run(host="0.0.0.0", port=5000)
