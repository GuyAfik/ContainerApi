
from core.api.common.database import container_db, DatabaseOperations


def container_model():
    return DatabaseOperations(collection_type=container_db['container'])


