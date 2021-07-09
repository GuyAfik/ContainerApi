"""
Here resides the business logic layer.
"""
import docker

from .persistence import insert_container_attrs
from core.api.common.middleware.response import response_decorator
from core.api.common.validation import BaseContainerSchema, validate_request_body

docker_client = docker.from_env()


@response_decorator(code=200)
@validate_request_body(schema_class=BaseContainerSchema)
def run_container(**container_data):
    """
    Creates a new container.

    Keyword Arguments:
        name (str): container name.
        image (str): container image.
        ports (dict): container ports.
        command (str): container command.
        detach (bool): detached state of the container, True to detach, False otherwise.

    Returns:
        dict: container information.
    """
    container = docker_client.containers.run(**container_data)

    if not container_data.get("detach"):  # this means that we got back the container logs instead of the object.
        container = docker_client.containers.get(container_id=container_data.get("name"))

    insert_container_attrs(container_attrs=container.attrs)

    return container.attrs

