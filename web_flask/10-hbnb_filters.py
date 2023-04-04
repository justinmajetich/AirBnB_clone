#!/usr/bin/python3
""" A script that starts a Flask web application with storage """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states_id():
    """ Get everything and show it """
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    list_city = []
    list_state = []
    list_amen = []
    city_item = storage.all(City).values()
    for city in city_item:
        list_city.append(city.to_dict())
    state_item = storage.all(State).values()
    for state in state_item:
        list_state.append(state.to_dict())
    amen_item = storage.all(Amenity).values()
    for ameni in amen_item:
        list_amen.append(ameni.to_dict())
    list_city = sorted(list_city, key=lambda d: d['name'])
    list_state = sorted(list_state, key=lambda d: d['name'])
    list_amen = sorted(list_amen, key=lambda d: d['name'])
    return render_template("10-hbnb_filters.html",
                           state_item=list_state, city_item=list_city, amen=list_amen)


@app.teardown_appcontext
def close_db(error):
    from models.engine.db_storage import DBStorage
    if isinstance(storage, DBStorage):
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
