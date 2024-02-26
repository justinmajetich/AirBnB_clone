#!/usr/bin/python3
"""index"""

from api.v1.views import app_views

@app.route('/status', methods=['GET'])
def status():
    """returns a JSON"""
    return jsonify({"status": "OK"})
