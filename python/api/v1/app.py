#!/usr/bin/env python3
"""
Flask Application
"""
import models
from api.v1.views import app_views
from flask import Flask, make_response, jsonify, request, abort
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)

auth = None
auth_type = environ.get('AUTH_TYPE')

if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
if auth_type == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()

@app.before_request
def before_request():
    """
    Filter each request before it's handled by proper route
    """
    if auth is None:
        abort(403)

    excluded = ['/api/v1/status', '/api/v1/stats',
                '/api/v1/auth_session/*']
    if auth.require_auth(request.path, excluded):
        cookie = auth.session_cookie(request)
        if auth.authorization_header(request) is None and cookie is None:
            abort(401)

        # print(auth_type)
        # print(auth.current_user)
        # print('user', auth.current_user(request))
        if auth.current_user(request) is None:
            abort(403)
    setattr(request, "current_user", auth.current_user(request))


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
        description: a resource was not found
    """
    return make_response(jsonify({"error": "Not Found"}), 404)


@app.errorhandler(403)
def forbidden(error):
    """ 403 Error
    ---
    responses:
      403:
        description: forbidden
    """
    return make_response(jsonify({"error": "Forbidden"}), 403)


@app.errorhandler(401)
def unauthorized(error):
    """ 401 Error
    ---
    responses:
      401:
        description: unauthorized
    """
    return make_response(jsonify({"error": "Unauthorized"}), 401)


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
