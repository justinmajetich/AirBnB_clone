#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""
# Import Flask
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Route decorator to map the URL route to a function
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
