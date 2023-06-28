#!/usr/bin/python3
""" Web application listening on the 0.0.0.0, port 5000 """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    print("states", states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
