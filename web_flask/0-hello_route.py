#!/usr/bin/python3


"""
Starts a Flask web app
"""
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the root URL and set strict_slashes to False


@app.route('/', strict_slashes=False)
def hello():
    # Function to be executed when the root URL is accessed
    return 'Hello HBNB!'


# Check if the script is run directly (not imported)
if __name__ == "__main__":
    # Start the Flask web server on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
