"""
Here resides the layer to interact with the DB.
"""
from .models import container_model


def insert_container_attrs(container_attrs):
    """
    Inserts a container document into the DB.
    """
    cm = container_model()
    cm.insert_document(document=container_attrs)


def get_last_container():
    """
    Gets the last created container.

    Returns:
        dict: last container information.
    """
    pass