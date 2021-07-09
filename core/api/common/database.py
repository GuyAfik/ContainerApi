
from pymongo import MongoClient, DESCENDING
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

    def get_last_document(self):
        """
        Gets the last document that was inserted to the DB.

        Returns:
             dict: the last inserted document

        Raises:
            ResourceNotFound: in case the database is empty.
        """
        # Using _id here to sort because the ObjectId values are always going to "increase" as they are added
        last_document = self._collection_type.find_one(sort=[('_id', DESCENDING)])
        if last_document:
            return last_document
        raise ResourceNotFound("Currently there isn't any record/document in the DB!")

    def get_all_documents(self):
        """
        Gets all the documents from the DB.

        Returns:
            list[dict]: a list of records documents, empty list incase there aren't any documents in the DB.
        """
        results = []
        all_documents_iter = self._collection_type.find({})

        for document in all_documents_iter:
            results.append(document)
        return results
