
class ApiException(Exception):
    """
    A base class for all api Exceptions.
    """
    status_code = None

    def __init__(self, message=None):

        self.message = message
        super().__init__(message)

    def to_dict(self):
        """
        represents the exception as a dictionary form.

        Returns:
            dict: a customized exception error details.
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
