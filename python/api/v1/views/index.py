#!/usr/bin/env python3
"""
Index
"""
import models
from models.user import User
from models.ride import Ride
from models.ride_request import RideRequest
from api.v1.views import app_views
from flask import make_response, jsonify, abort, render_template


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
    classes = [User, Ride, RideRequest]
    names = ['users', 'rides', 'ride requests']

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = models.storage.count(classes[i])
    return make_response(jsonify(num_objs), 200)


@app_views.route("/tos", methods=["GET"], strict_slashes=False)
def tos():
    """
    Terms and Conditions
    """
    try:
        with open('../LICENSE', mode='r', encoding='utf-8') as file:
            file = file.readlines()
            # for line in file:
            #     print(line)
            return render_template('license.html',
                                   data={"title":"Terms and Conditions",
                                         "message":file})
    except Exception as e:
        print(str(e))
        abort(404)
