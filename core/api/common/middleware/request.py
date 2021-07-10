from flask import request
from .response import make_server_response
from core.api.common.exceptions import InvalidContentType


def ensure_content_type():
    """
    Ensures that the Content-Type for all requests is `application-json`, otherwise appropriate error is raised.

    Returns:
        Response: response indicating about invalid content-type, None otherwise.
    """
    content_type = request.headers.get('Content-type')
    # content type should not be verified on 'GET' requests.
    if not content_type == 'application/json' and request.method != 'GET':
        invalid_content_type = InvalidContentType(message='Invalid content-type. Only `application-json` is allowed.')
        return make_server_response(invalid_content_type.to_dict(), http_status_code=invalid_content_type.status_code)
