from pymongo import MongoClient
from .exceptions import InsertDatabaseError, ResourceNotFound

# for local host

# TODO - use env variable for that
# db_client = MongoClient(os.environ.get("MONGO_DB_URI"))
db_client = MongoClient(
    "mongodb+srv://Metasploit:FVDxbg312@metasploit.gdvxn.mongodb.net/metasploit?retryWrites=true&w=majority"
)

# container_db = db_client[os.environ.get("DATABASE")]
container_db = db_client['ContainerApi']


class DatabaseOperations(object):
    """
    Class to manage all database operations.

    Attributes:
        collection_type (pymongo.Collection): the collection to use in the DB.
    """
    def __init__(self, collection_type):
        """
        Initialize the DatabaseOperations class attributes.

        Args:
            collection_type (pymongo.Collection): the collection to use to access/modify DB documents.
        """
        self._collection_type = collection_type

    def insert_document(self, document):
        """
        Inserts a document into the DB.

        Raises:
            InsertDatabaseError: in case insertion to the DB fails.
        """
        try:
            self._collection_type.insert_one(document=document)
        except Exception as error:
            raise InsertDatabaseError(message=str(error))

    def get_document(self, _id, type='container'):
        """
        Gets a document from the DB.

        Args:
            _id (str): ID of the resource.
            type (str): type of the resource. e.g.: 'container'

        Returns:
            dict: a document that matches the resource ID.

        Raises:
            ResourceNotFound: in case the resource was not found in the DB.
        """
        found_document = self._collection_type.find_one(filter={"_id": _id})
        if found_document:
            return found_document
        else:
            raise ResourceNotFound(message=f"{type} with ID {_id} does not exist")

