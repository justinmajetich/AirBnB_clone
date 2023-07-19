#!/usr/bin/python3
"""
Currently, this is jsut a copy of task 9 (as assigned, task names are off by 1.)
script that starts a Flask web application

Your web application must be listening on 0.0.0.0, port 5000

You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage
    and
    storage.all(...)

After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
        In this method, call "storage.close()"


Routes:

    /states_list: display a HTML page:
        inside tag body:
            H1 tag: “States”
            UL tag:
                with the list of
                    all State objects present in DBStorage
                        sorted by name (A->Z)
                LI tag:
                description of one State:
                    <state.id>: <B><state.name></B>

    /cities_by_states
        its essentially the same as states above, but the cities nested within

You must use the option strict_slashes=False in your route definition.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exception):
    """method to handle
    @app.teardown_appcontext
    Call in this method: storage.close()
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    summons html page to list all
    State objects present in DBStorage
    sorted by name (A->Z)

    list all city objects within each state object
    because the city is within state, it is included in a state already
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
