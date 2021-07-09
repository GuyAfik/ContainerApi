from flask import request
from core.api.common.exceptions import InvalidContentType


def ensure_content_type():
    """
    Ensures that the Content-Type for all requests is `application-json`, otherwise appropriate error is raised.

    Raises:
        InvalidContentType: if Content-Type is not `application-json`
    """
    content_type = request.headers.get('Content-type')
    if not content_type == 'application/json':
        raise InvalidContentType(
            message='Invalid content-type. Only `application-json` is allowed.'
        )

