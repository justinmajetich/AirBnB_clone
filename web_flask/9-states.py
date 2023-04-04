#!/usr/bin/python3
""" A script that starts a Flask web application with storage """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    from models.state import State
    list_state = []
    state_item = storage.all(State).values()
    for state in state_item:
        list_state.append(state.to_dict())
    list_state = sorted(list_state, key=lambda d: d['name'])
    return render_template("7-states_list.html", state_item=list_state)
    
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    from models.state import State
    from models.city import City
    
    list_city = []
    state_obj = None
    is_found = False

    state_item = storage.all(State).values()
    for state in state_item:
        obj = state.to_dict()
        if obj.get("id") == id:
            state_obj = obj
            is_found = True
    
    city_item = storage.all(City).values()
    for city in city_item:
        if city.to_dict().get("state_id") == id:
            list_city.append(city.to_dict())


    list_city = sorted(list_city, key=lambda d: d['name'])
    return render_template("9-states.html",
                            state_item=state_obj, city_item=list_city, is_found=is_found)
    


@app.teardown_appcontext
def close_db(error):
    from models.engine.db_storage import DBStorage
    if isinstance(storage, DBStorage):
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
