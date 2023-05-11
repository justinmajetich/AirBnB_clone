#!/usr/bin/python3
"""
 Script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
     (FileStorage or DBStorage)=>from models import storage & storage.all(...)
    To load all cities of a State:
        If your storage engine is DBStorage, you must use cities relationship
        Otherwise, use the public getter method cities
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /hbnb_filters: display a HTML page like 6-index.html, which was done
         during the project 0x01. AirBnB clone - Web static
            Copy files 3-footer.css, 3-header.css, 4-common.css and
             6-filters.css from web_static/styles/ to folder
              web_flask/static/styles
            Copy files icon.png and logo.png from web_static/images/ to the
             folder web_flask/static/images
            Update .popover class in 6-filters.css to allow scrolling in the
             popover and a max height of 300 pixels.
            Use 6-index.html content as source code for the template
             10-hbnb_filters.html:
                Replace the content of the H4 tag under each filter title
                 (H3 States and H3 Amenities) by &nbsp;
            State, City and Amenity objects must be loaded from DBStorage and
             sorted by name (A->Z)
    You must use the option strict_slashes=False in your route definition
    Import this 10-dump to have some data

IMPORTANT

    Make sure you have a running and valid setup_mysql_dev.sql in your
     AirBnB_clone_v2 repository (Task)
    Make sure all tables are created when you run echo "quit" |
     HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd
     HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db
     HBNB_TYPE_STORAGE=db ./console.py
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/hbnb_filters/', strict_slashes=False)
def display_html():
    """ Function called with /states route """
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html',
                           states=states.values(),
                           amenities=amenities.values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
