from flask import make_response, jsonify
from ..exceptions import ApiException


def response_decorator(code):
    """
    Decorator to execute all the API services implementations and parse a valid response to them.

    Args:
        code (int): http code that should indicate about success.

    Returns:
        Response: flask api response.
    """
    def decorator(func):

        def wrapper(*args, **kwargs):

            http_status_code = code
            try:
                response = func(*args, **kwargs)
            except ApiException as error:
                response = error.to_dict()
                http_status_code = error.status_code
            return make_server_response(response=response, http_status_code=http_status_code)

        return wrapper
    return decorator


def make_server_response(response, http_status_code):
    """
    Returns an API response for the client.

    Args:
        response (list/dict/serializable object): api response for the client.
        http_status_code (int): the http status code that the server should return.

    Returns:
        Response: a flask response.
    """
    return make_response(jsonify(response), http_status_code)
