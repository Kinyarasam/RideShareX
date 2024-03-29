#!/usr/bin/env python3
"""
objects that handle all default RestFul API actions for ride requests
"""
import models
from models.ride import Ride
from models.ride_request import RideRequest
from api.v1.views import app_views
from flask import request, make_response, jsonify, abort


@app_views.route("/rides/<ride_id>/requests", methods=["GET"], strict_slashes=False)
def all_requests(ride_id):
    """
    Retrieves a list of all ride requests by a given user
    """
    user = request.current_user
    if not user:
        abort(403)
    all_user_ride_requests = models.storage.all(RideRequest).values()
    ride = models.storage.get(Ride, ride_id).to_dict()
    list_requests = []
    for ride_request in all_user_ride_requests:
        if ride_request.ride_id == ride_id and ride_request.user_id == user.id:
            list_requests.append(ride_request.to_dict())
    ride["requests"] = list_requests
    return make_response(jsonify(ride), 200)

@app_views.route("/rides/<ride_id>/requests")
def post_requests(ride_id):
    """
    Create a ride request
    """
