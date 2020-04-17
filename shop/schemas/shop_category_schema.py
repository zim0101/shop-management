from marshmallow import Schema, fields


class ShopCategoryCreateSchema(Schema):
    """
        ShopCategory create schema
    """
    name = fields.Str(required=True)


class ShopCategoryEditSchema(Schema):
    """
        ShopCategory edit schema
    """
    name = fields.Str()
