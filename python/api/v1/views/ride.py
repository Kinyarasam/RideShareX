#!/usr/bin/env python3
"""
objects that handle all default RestFul API actions for rides
"""
import models
from api.v1.views import app_views
from models.ride import Ride
from flask import make_response, jsonify, abort, request


@app_views.route("/rides", methods=["GET"], strict_slashes=False)
def all_rides():
    """
    Retrieves a list of all ride objects
    or a specific ride
    """
    all_rides = models.storage.all(Ride).values()
    list_rides = []
    for ride in all_rides:
        list_rides.append(ride.to_dict())
    return make_response(jsonify(list_rides), 200)


@app_views.route("/rides/<ride_id>", methods=["GET"], strict_slashes=False)
def get_ride(ride_id):
    """
    Retrieve a ride
    """
    ride = models.storage.get(Ride, ride_id)
    if not ride:
        abort(404)
    return make_response(jsonify(ride.to_dict()), 200)


@app_views.route("/rides", methods=["POST"], strict_slashes=False)
def post_ride():
    """
    Creates a ride
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'plate_no' not in request.get_json():
        abort(400, description="missing plate_no")
    
    data = request.get_json()
    instance = Ride(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route("/rides/<ride_id>", methods=["PUT"], strict_slashes=False)
def put_ride(ride_id):
    """
    Updates a ride
    """
    ride = models.storage.get(Ride, ride_id)
    if not ride:
        abort(404)
    if not request.get_json():
        abort(404, description="Not a JSON")

    ignore = ["id", "created_at", "updated_at", "plate_no"]
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(ride, key, value)
    ride.save()
    return make_response(jsonify(ride.to_dict()), 201)


@app_views.route("/rides/<ride_id>", methods=["DELETE"], strict_slashes=False)
def delete_ride(ride_id):
    """
    Deletes a ride object
    """
    ride = models.storage.get(Ride, ride_id)
    if not ride:
        abort(404)

    models.storage.delete(ride)
    models.storage.save()
    return make_response(jsonify({}), 200)
