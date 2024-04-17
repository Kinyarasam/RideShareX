#!/usr/bin/env python3
"""
Flask Application
"""
import models
from api.v1.views import app_views
from flask import Flask, make_response, jsonify, request, abort
from os import environ
from flasgger import Swagger


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
                '/api/v1/auth_session/*', '/apidocs*',
                '/flasgger*', '/apispec*', '/favicon*',
                '/api/v1/tos']
    if auth.require_auth(request.path, excluded):
        cookie = auth.session_cookie(request)
        if auth.authorization_header(request) is None and cookie is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)
    setattr(request, "current_user", auth.current_user(request))


@app.teardown_appcontext
def close_db(error):
    """
    Close storage
    """
    models.storage.close()


@app.errorhandler(405)
def not_allowed(error):
    """405 Error
    ---
    responses:
      405:
        description: Method Not Allowed.
    """
    return make_response(jsonify({"error": "Method Not Allowed"}), 405)


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


@app.errorhandler(400)
def bad_request(error):
    """400 Error
    ---
    responses:
      400:
        description: bad request
    """
    return make_response(jsonify({"error": "Bad Request!"}), 400)


app.config["SWAGGER"] = {
    "title": "RideShareX",
    "uiversion": 3,
    "description": """
## Description
RideShareX is a robust and feature-rich ride-sharing service built with Java, designed to simplify urban commuting. Our platform seamlessly connects riders with nearby drivers, offering real-time tracking, secure payments, and a user-friendly experience. With integrated mapping services, users can track rides in real-time, ensuring a smooth and efficient journey from start to finish

## Key Features:

* __Real-Time:__ Tracking: Track your ride and driver's location in real-time using integrated mapping services.
* __Smart Matching:__ Efficiently match riders with available drivers based on proximity and ride preferences.
* __Transparent Fare Calculation:__ Estimate fares based on distance, duration, and traffic conditions before confirming the ride.
* __Secure Payments:__ Process payments securely through multiple payment methods, ensuring a hassle-free transaction experience.
* __User Reviews:__ Rate drivers and leave reviews to maintain a high-quality ride experience for all users.

## Technologies Used:
Java, Spring Framework, Hibernate, Google Maps API, MySQL, HTML/CSS, Javascript

## How to Contribute:
We welcome contributions from developers of all levels! Check out our [Contribution Guidelines](./docs/CONTRIBUTION.md) to get started. Whether you're passionate about frontend design, backend development, or testing, there's a place for you in our community.

## Installation and usage:
Detailed instructions on how to install, configure and use RideShareX can be found in our [documentation](./docs/INSTALLATION.md).

## License:
This project is licensed under the [MIT License](./tos) - see the [LICENSE](./LICENSE) file for details.

## Contact:
Have questions or suggestions? Feel free to reach out to us at <mailto>skinyara.30@gmail.com</mailto>.

_Join us in revolutionizing urban transportation with **RideShareX!**_
""",
    "termsOfService": "/api/v1/tos"
}

Swagger(app)


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
