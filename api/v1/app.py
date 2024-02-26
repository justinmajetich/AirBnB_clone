#!/usr/bin/python3
"""status of your api"""
import os
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)


app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(exception):
    """teat down"""
    storage.close()

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)

