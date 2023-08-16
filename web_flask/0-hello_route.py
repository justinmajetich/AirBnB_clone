#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/', methods=['GET'], strict_slashes=False)
def hello():
    """ a function that display Hello HBNB! """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
