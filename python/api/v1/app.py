#!/usr/bin/env python3
"""
Flask Application
"""
import models
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """
    Close storage
    """
    models.storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a reaource was not found
    """
    return make_response(jsonify({"error": "Not Found"}), 404)


if __name__ == "__main__":
    """
    Main Function
    """
    host = environ.get("RIDESHARE_API_HOST")
    port = environ.get("RIDESHARE_API_PORT")
    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"
    app.run(host=host, port=port, threaded=True, debug=True)
