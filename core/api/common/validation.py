
from marshmallow import Schema, fields, ValidationError
from .exceptions import InvalidJsonBodyRequest


class BaseContainerSchema(Schema):
    """
    Base container schema class for the validation of json body request.
    """
    name = fields.String(required=True)
    image = fields.String(required=True)
    ports = fields.Dict()
    detach = fields.Boolean(missing=True)


def validate_request_body(schema_class):
    """
    Validates that the json body request is well formed & parse the input client json to the correct schema class.

    Args:
         schema_class (Schema): the class type (cls) of the schema. e.g.: schema_class = BaseContainerSchema.

    Raises:
        InvalidJsonBodyRequest: in case the json body request provided is not valid.
    """
    def decorator(func):

        def wrapped(**kwargs):
            try:
                data = schema_class().load(kwargs)
            except ValidationError as err:
                raise InvalidJsonBodyRequest(message=str(err))
            return func(**data)
        return wrapped
    return decorator

