from marshmallow import Schema, fields, validate


class NewRouteSchema(Schema):
    """
    :parameter
        - source (str)
        - destination (str)
        - cost (int)
    """

    source = fields.Str(validate=validate.Length(min=1))
    destination = fields.Str(validate=validate.Length(min=1))
    cost = fields.Int(validate=validate.Range(min=0))


class BestRouteSchema(Schema):
    """
    :parameter
        - source (str)
        - destination (str)
    """

    source = fields.Str(validate=validate.Length(min=1))
    destination = fields.Str(validate=validate.Length(min=1))
