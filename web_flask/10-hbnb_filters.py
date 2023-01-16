#!/usr/bin/python3
"""Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage
        engine (FileStorage or DBStorage) =>
        from models import storage and storage.all(...)
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(execption):
    """Closes the database"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    return render_template(
        "10-hbnb_filters.html",
        states=sorted(storage.all(State).values(), key=lambda d: d.name),
        amenities=sorted(storage.all(Amenity).values(), key=lambda d: d.name)
    )
