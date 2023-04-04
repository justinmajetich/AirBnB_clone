#!/usr/bin/python3
""" A script that starts a Flask web application with storage """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def listing():
    from models.state import State
    lol = []
    states = storage.all(State).values()
    for state in states:
        lol.append(state.to_dict())
    return render_template("7-states_list.html", state_item=lol)


@app.teardown_appcontext
def close_db(error):
    from models.engine.db_storage import DBStorage
    if isinstance(storage, DBStorage):
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
