from marshmallow import Schema, fields


class ShopCreateSchema(Schema):
    """
        Shop create schema
    """
    name = fields.Str(required=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    address = fields.Str(required=True)
    size = fields.Int(required=True)


class ShopEditSchema(Schema):
    """
        Shop edit schema
    """
    name = fields.Str()
    user_id = fields.Int()
    category_id = fields.Int()
    address = fields.Str()
    size = fields.Int()
