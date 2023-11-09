#!/user/bin/python3
"""Starts a Flask web app"""

from flask import Flask

app = Flask(__name__)


"""Define the route for the root URL '/'"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == "__main__":
    """Start the Flask development server"""
    app.run(host='0.0.0', port=5000)