
from flask import request
from marshmallow import Schema, fields, ValidationError
from .exceptions import InvalidJsonBodyRequest


class BaseContainerSchema(Schema):
    name = fields.String(required=True)
    image = fields.String(required=True)
    port = fields.Dict(keys=fields.Str(), values=fields.Str())
    detach = fields.Boolean(default=False)


def validate_request_body(schema_class):
    """
    Validates that the json body request is well formed.

    Args:
         schema_class (Schema): the class type of the schema. e.g.: schema_class = BaseContainerSchema.

    Raises:
        InvalidJsonBodyRequest: in case the json body request provided is not valid.
    """
    def decorator(func):

        def wrapped(*args, **kwargs):
            try:
                schema_class().load(request.json)
            except ValidationError as err:
                raise InvalidJsonBodyRequest(message=str(err))
            return func(*args, **kwargs)
        return wrapped
    return decorator

