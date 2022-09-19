#!/usr/bin/python3
"""script that starts a Flask web application"""

from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def app_teardown(self):
    """method that calls storage.close()"""
    storage.close()


@app_views.app_errorhandler(404)
def not_found(e):
    """Page not found."""
    resp = {"error": "Not found"}
    return jsonify(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
