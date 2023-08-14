#!/usr/bin/python3
"""Import Modules"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Main Route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route hbnb"""
    return 'HBNB'


"""Entry Point"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
