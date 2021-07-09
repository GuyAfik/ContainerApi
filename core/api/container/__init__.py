from flask import Blueprint

BP_NAME = "container"
container_blueprint = Blueprint(BP_NAME, __name__)

from . import views
