#!/usr/bin/python3
"""initializing file"""
from flask import Flask

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Import routes
    from . import routes

    # Register routes
    app.register_blueprint(routes.bp)

    return app

