
class ApiException(Exception):
    """
    A base class for all api Exceptions.
    """
    status_code = None

    def __init__(self, message=None):

        self.message = message
        super().__init__(message)

    def __str__(self):
        """
        converts the exception into a string representation.

        Returns:
            str: string representation of the exception.
        """
        if self._is_client_error():
            return f"Client Error: {self.message}"
        return f"Server Error: {self.message}"

    def _is_client_error(self):
        """
        Checks if the error is a client error.

        Returns:
            bool: True if status code is a client error, False otherwise.
        """
        return 400 <= self.status_code < 500

    def to_dict(self):
        """
        represents the exception as a dictionary form.
        """
        return {
            'error': {
                'code': self.status_code,
                'message': self.message,
                'type': str(self.__class__.__name__)
            }
        }


class InvalidContentType(ApiException):
    """
    Raised when an invalid content type is provided.
    """
    status_code = 400


class InvalidJsonBodyRequest(ApiException):
    """
    Raises when an invalid body request is provided.
    """
    status_code = 400


class DatabaseErrors(ApiException):
    """
    Raises when a database error occurs
    """
    status_code = 500


class InsertDatabaseError(DatabaseErrors):
    """
    Raises when there is a database insertion error
    """
    pass


class ResourceNotFound(ApiException):
    """
    Raises when there is a resource that was not found in the DB.
    """
    status_code = 404
