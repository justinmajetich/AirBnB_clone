#!/usr/bin/python3
""" A script that starts a Flask web application with storage """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states")
def cities_by_state():
    from models.state import State
    from models.city import City
    list_city = []
    list_state = []
    city_item = storage.all(City).values()
    for city in city_item:
        list_city.append(city.to_dict())
    state_item = storage.all(State).values()
    for state in state_item:
        list_state.append(state.to_dict())
    list_city = sorted(list_city, key=lambda d: d['name'])
    list_state = sorted(list_state, key=lambda d: d['name'])
    return render_template("8-cities_by_states.html",
                           state_item=list_state, city_item=list_city)


@app.teardown_appcontext
def close_db(error):
    from models.engine.db_storage import DBStorage
    if isinstance(storage, DBStorage):
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
