#!/usr/bin/env python3
"""
objects that handle all default RestFul API actions for users
"""
import models
from api.v1.views import app_views
from models.user import User
from flask import make_response, jsonify, abort, request


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def all_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = models.storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return make_response(jsonify(list_users), 200)


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def get_users(user_id):
    """
    Retrieves an user
    """
    if user_id == "me":
        if request.current_user is None:
            abort(404)
        user = request.current_user
        return make_response(jsonify(user.to_dict()), 200)
    user = models.storage.get(User, user_id)
    if not user:
        abort(404)
    return make_response(jsonify(user.to_dict()), 200)


@app_views.route("/users", methods=["POST"], strict_slashes=False)
def post_user():
    """
    Creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    if 'first_name' not in request.get_json():
        abort(400, description="Missing first_name")
        
    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def put_user(user_id):
    """
    Updates a user
    """
    user = models.storage.get(User, user_id)
    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ["id", "email", "created_at", "updated_at"]
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a user object
    """
    user = models.storage.get(User, user_id)
    if not user:
        abort(404)

    models.storage.delete(user)
    models.storage.save()
    return make_response(jsonify({}), 200)
