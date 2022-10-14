from flask import Flask
from models import storage
from flask import render_template
"""
A simple flask server running on 0.0.0.0:5000
"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_current_session(exc):
    storage.close()


@app.route('/states_list')
def display_states():
    """Prints html document with a list of states"""
    states = storage.all('State')
    return render_template('7-states_list.html', state_list=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
