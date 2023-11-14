#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from models import storage
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays list of states and cities from DB """
    all_cities = storage.all(City)
    list_cities = []

    for x in all_cities.values():
        list_cities.append(x)

    return render_template(
        '8-cities_by_states.html',
        states=list_cities
    )


@app.teardown_appcontext
def teardown(error=None):
    """ Closes current storage """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
