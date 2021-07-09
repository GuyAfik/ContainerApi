"""
Here will be the data model layer where all blueprint models are defined.
"""
from core.api.common.database import container_db, DatabaseOperations


def container_model():
    """
    Returns the DatabaseOperations object based on the container collection.

    Returns:
        DatabaseOperations: database operations object.
    """
    return DatabaseOperations(collection_type=container_db['container'])


