#!/usr/bin/python3
'''
Start a Flask web application
'''
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = '5000'


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''
    list states or show details of a particular state
    '''
    template = '10-hbnb_filters.html'
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(template, states=states, amenities=amenities)


@app.teardown_appcontext
def close_storage(exc):
    '''
    close storage
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
