#!/usr/bin/python3
"""
 Script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage & storage.all(..)
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in DBStorage
              sorted by name (A->Z) tip
                LI tag: description of State: <state.id>:<B><state.name></B>
    Import this 7-dump to have some data
    You must use the option strict_slashes=False in your route definition

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


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_html():
    """ Function called with /states_list route """
    states = storage.all(State)
    dict_to_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=dict_to_html)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
