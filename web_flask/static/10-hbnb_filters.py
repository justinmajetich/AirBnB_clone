from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def close_session(exception=None):
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states = sorted(storage.all(State), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity), key=lambda amenity: amenity.name)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

