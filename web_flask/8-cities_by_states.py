#!/usr/bin/python3
"""Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /cities_by_states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name></B>
            + UL tag: with the list of City objects linked to the State
            sorted by name (A->Z)
                LI tag: description of one City: <city.id>: <B><city.name></B>
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(execption):
    """Closes the database"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """display a HTML page: (inside the tag BODY)"""
    states = sorted(storage.all(State).values(), key=lambda d: d.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda d: d.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
