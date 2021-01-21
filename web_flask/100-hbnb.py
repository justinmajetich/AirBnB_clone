#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters(id='0'):
        return render_template("100-hbnb.html",
                               states=storage.all(State).values(),
                               amenities=storage.all(Amenity).values(),
                               places=storage.all(Place).values())


@app.teardown_appcontext
def close():
        storage.close()

if __name__ == "__main__":
        app.run(debug=True)
