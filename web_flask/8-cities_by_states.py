#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    from models.city import City
    """ Displays list of states and cities from DB """
    storage.reload()
    all_cities = storage.all(City)
    list_cities = []

    for x in all_cities:
        all_cities.append(all_cities[x])

    return render_template(
        '8-cities_by_states.html',
        storage.all == list_cities
    )


@app.teardown_appcontext
def teardown(error=None):
    """ Closes current storage """
    current_storage = getattr(g, "storage", None)
    if current_storage is not None:
        g.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
