"""
Here resides the business logic layer.
"""
import docker

from . import persistence
from core.api.common.middleware.response import response_decorator
from core.api.common.validation import BaseContainerSchema, validate_request_body

docker_client = docker.from_env()


@response_decorator(code=200)
@validate_request_body(schema_class=BaseContainerSchema)
def run_container(**container_data):
    """
    Creates & runs a new container.

    Keyword Arguments:
        name (str): container name.
        image (str): container image.
        ports (dict): container ports.
        command (str): container command.
        detach (bool): detached state of the container, True to detach, False otherwise.

    Json examples:
        {
            "name": "my_nginx",
            "image": "nginx",
            "ports": {
                "22222/tcp": 22222
            }
        }

        {
            "name": "hello-world-container",
            "image": "hello-world",
            "detach": false
        }

    Curl examples:

        You can run container with any image that you like, here are two examples:

        Hello world container:

        curl -d '{"name": "my_nginx", "image": "hello-world"}' -H "Content-Type: application/json" -X POST
        http://<server_ip>:<server_port>/Container

        nginx container:

        curl -d '{"name": "bla1", "image": "nginx", "ports": {"22222/tcp": 22222}, "detach": true}' -H
        "Content-Type: application/json" -X POST http://<server_ip>:<server_port>/Container

    Notes:
        name & image json fields when trying to run a container are required! even though name can be atomically created
        by the docker. In my opinion its important to have a container meaningful name in order to know what it does.

    Returns:
        dict: container information.
    """
    container = docker_client.containers.run(**container_data)

    if not container_data.get("detach"):  # this means that we got back the container logs instead of the object.
        container = docker_client.containers.get(container_id=container_data.get("name"))
    # persistence.insert_container_attrs(container_attrs=container.attrs)

    return container.attrs


@response_decorator(code=200)
def get_latest_running_container(limit=1):
    """
    Gets the latest running container.

    Args:
        limit (int): the amount of last containers to get.

    Returns:
        dict: last container information in case found, empty dict otherwise.
    """
    container = docker_client.containers.list(limit=limit)
    if container:
        return container[0].attrs
    return {}
    # return persistence.get_last_container()


@response_decorator(code=200)
def get_all_containers():
    """
    Gets all the containers.

    Returns:
         list[dict]: all containers.
    """
    return [container.attrs for container in docker_client.containers.list(all=True)]
    # return persistence.get_all_containers()

