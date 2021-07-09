"""
Here resides the layer to interact with the DB.
"""
from .models import container_model


def insert_container_attrs(container_attrs):
    """
    Inserts a container document into the DB.

    Args:
        container_attrs (dict): container attributes information.
    """
    container_model().insert_document(document=container_attrs)


def get_last_container():
    """
    Gets the last created container document.

    Returns:
        dict: last container information.
    """
    return container_model().get_last_document()


def get_all_containers():
    """
    Gets all of the container documents.

    Returns:
         list[dict]: all of the container documents.
    """
    return container_model().get_all_documents()
