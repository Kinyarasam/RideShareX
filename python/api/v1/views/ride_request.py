#!/usr/bin/env python3
"""
objects that handle all default RestFul API actions for ride requests
"""
import models
from api.v1.views import app_views
from models.ride_request import RideRequest


@app_views.route("/rides/<ride_id>/requests")
def all_requests(ride_id):
    """

    """