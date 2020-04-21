from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    class Meta:
        fields = (
            "id",
            "name",
            "username",
            "password",
            "role",
            "email_verified",
            "created_at"
        )


class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
