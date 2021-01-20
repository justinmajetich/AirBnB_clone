#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.state import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """ close storage """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False, methods=["GET", "POST"])
def state_list():
    """ route to display a HTML page """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
