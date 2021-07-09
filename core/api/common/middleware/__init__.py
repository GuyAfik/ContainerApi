from .request import ensure_content_type


def before_request_middleware(app):
    app.before_request_funcs.setdefault(None, [ensure_content_type])
