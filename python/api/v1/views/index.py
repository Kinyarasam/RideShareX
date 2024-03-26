#!/usr/bin/env python3
"""
Index
"""
import models
from api.v1.views import app_views
from flask import make_response, jsonify


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    Status of the API
    """
    return make_response(jsonify({"status": "OK"}), 200)


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
    """
    Retrieves the number of each objects by type
    """
    classes = []
    names = []

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = models.storage.count(classes[i])
    return make_response(jsonify(num_objs), 200)
