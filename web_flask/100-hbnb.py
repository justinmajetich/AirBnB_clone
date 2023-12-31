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
from models.city import City
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(execption):
    """Closes the database"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return render_template(
        "100-hbnb.html",
        amenities=sorted(storage.all(Amenity).values(), key=lambda d: d.name),
        cities=sorted(storage.all(City).values(), key=lambda d: d.name),
        places=sorted(storage.all(Place).values(), key=lambda d: d.name),
        states=sorted(storage.all(State).values(), key=lambda d: d.name),
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0")
