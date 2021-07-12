from .request import ensure_content_type


def before_request_middleware(app):
    """
    This function will be executed before each request to validate the content type.

    Args:
        app (Flask): flask application.
    """
    app.before_request_funcs.setdefault(None, [ensure_content_type])
