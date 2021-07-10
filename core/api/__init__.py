

from flask import Flask
from .common.middleware import before_request_middleware
from .container import container_blueprint as container_bp


def create_app():
    """
    Creates a new flask application with customized parameters.

    Returns:
        app: Flask object.
    """
    app = Flask(__name__)

    app.register_blueprint(blueprint=container_bp)

    before_request_middleware(app=app)

    return app
