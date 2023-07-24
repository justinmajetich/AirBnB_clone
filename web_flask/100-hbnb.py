from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
