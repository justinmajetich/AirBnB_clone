#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters(id='0'):
        return render_template("10-hbnb_filters.html",
                               states=storage.all(State).values(),
                               amenities=storage.all(Amenity).values(), id=id)


@app.teardown_appcontext
def close():
        storage.close()

if __name__ == "__main__":
        app.run(debug=True)
