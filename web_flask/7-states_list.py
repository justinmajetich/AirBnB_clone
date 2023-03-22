#!/usr/bin/python3
"""
Script that starts a Flask web application
    - listening on 0.0.0.0, port 5000
    - /states_list: display a HTML page: (inside the tag BODY)
        * H1 tag: “States”
        * UL tag: with the list of all State objects present in
        DBStorage sorted by name (A->Z) tip
            * LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list_route():
    """Method that displays a HTML page of States"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
