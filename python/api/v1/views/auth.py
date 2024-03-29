#!/usr/bin/env python3
"""
objects that will handle all default RestFul API actions for authentications
"""
import models
from models.user import User
from api.v1.views import app_views
from flask import request, abort, make_response, jsonify
from base64 import b64decode
from utils import session
from uuid import uuid4
from os import environ


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """
    Authenticates a user
    """
    from api.v1.app import auth
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(400, description="missing required parameters")

    auth_data = auth_header.split(' ')
    if len(auth_data) != 2:
        abort(400, description="missing required parameters")
    
    email, password = None, None
    try:
        email, password = b64decode(auth_data[1]).decode('utf-8').split(":")
    except:
        ...

    if email is None and password is None:
        abort(400, description="missing required parameters")

    user = User.find(email=email, password=password)
    if not user:
        abort(404, description="Invalid credentials")

    resp = jsonify(user.to_dict())
    session_id = auth.create_session(user.id)
    session_name = environ.get('SESSION_NAME')
    resp.set_cookie(session_name, session_id)

    return make_response(resp, 200)