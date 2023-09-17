#!/usr/bin/python3
"""
Index views
"""
from flask import jsonify, Blueprint

from api.v1.views import app_views

api_views = Blueprint('api_views', __name__)


@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
