"""
This module only know about HTTP requests and responses. The purpose here is to process a request and pass data
to lower layers and to return responses from lower layers.
"""
from flask import request
from . import logic
from . import container_blueprint


@container_blueprint.route('/container', methods=['POST'])
def run_container():
    """
    Run container endpoint.

    Returns:
        dict: the newly created container information.
    """
    return logic.run_container(**request.json)


@container_blueprint.route('/container', methods=['GET'])
def get_last_container():
    """
    Get last container record endpoint.

    Returns:
        dict: the last running container
    """
    return logic.get_latest_running_container()


@container_blueprint.route('/containers', methods=['GET'])
def get_all_containers():
    """
    Get all of the container records endpoint.

    Returns:
         list[dict]: all container records.
    """
    return logic.get_all_containers()
