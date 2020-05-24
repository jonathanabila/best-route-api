from marshmallow import Schema, fields


class NewRouteSchema(Schema):
    """
    :parameter
        - source (str)
        - destination (str)
        - cost (int)
    """

    source = fields.Str()
    destination = fields.Str()
    cost = fields.Int()


class BestRouteSchema(Schema):
    """
    :parameter
        - source (str)
        - destination (str)
    """

    source = fields.Str()
    destination = fields.Str()
