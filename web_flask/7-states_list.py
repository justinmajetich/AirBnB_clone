#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
Use storage for fetching data from the storage engine File or DB storage
from models import storage and storage.all(...)
After each request, remove current SQLAlchemy Session:
    Declare method to handle @app.teardown_appcontext
    Call in this method: storage.close()
Route /states_list: display a HTML page
    H1 tag: "States"
    UL tag: list of all State objects present in DBStorage sorted by name
        LI tag: Description of one State: <state.id>: <<B><state.name></B>
Must use option strict_slashes=False
"""
from models import storage
from models.state import State
from flask import render_template, Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list", strict_slashes=False)
def state_list():
    """
    Displays HTML formatted list of states from DB
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    Remove current SQLALchemy sesh
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
