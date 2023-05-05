#!/usr/bin/python3
"""
Python script to create and serve a simple web app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello():
    """
    Handles request to root URL

    Returns:
        str: Text found in this function
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    """
    Start the development server.
    """
    app.run(host='0.0.0.0', port=5000)
