#!/usr/bin/python3
""" A script that starts a Flask web application with storage """
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def listing():
    from models.state import State

    State_item = storage.all(State)
    niice = {}
    var_id = ""
    var_name = ""
    for _, v in State_item.items():
        for k, x in v.to_dict().items():
            if k == "id":
                var_id = x
            if k == "name":
                var_name = x
                niice[var_id] = var_name
    # print(niice)
    sorted_nice = dict(sorted(niice.items(), key=lambda item: item[1]))
    return render_template("7-states_list.html", state_item=sorted_nice)


@app.teardown_appcontext
def close_db(error):
    from models.engine.db_storage import DBStorage
    if isinstance(storage, DBStorage):
        storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
