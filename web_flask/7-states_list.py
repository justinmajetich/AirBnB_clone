#!/usr/bin/python3
"""
You must use storage for fetching data from
the storage engine (FileStorage or DBStorage) =>
from models import storage and storage.all(...)
"""
from models import storage
from flask import render_template, Flask

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    /states_list: display a HTML page: (inside the tag BODY)
    """
    states = storage.all('State')
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
