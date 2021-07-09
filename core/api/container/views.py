"""
This module only know about HTTP requests and responses. The purpose here is to process a request and pass data
to lower layers and to return responses from lower layers.
"""
from flask import request
from . import logic
from . import container_blueprint


@container_blueprint.route('/Container', methods=['POST'])
def run_container():
    """
    Run container endpoint.
    """
    return logic.run_container(**request.json)

