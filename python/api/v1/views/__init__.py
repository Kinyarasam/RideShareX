#!/usr/bin/env python3
"""
Blueprint for API
"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


from api.v1.views.auth import *
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.ride import *
from api.v1.views.ride_request import *
