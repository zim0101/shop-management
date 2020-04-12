from flask import jsonify
from user.schemas import UserSchema, UserLoginSchema


user_login_schema = UserLoginSchema()
user_schema = UserSchema()


class UserDataValidation:

    @staticmethod
    def user_login_data_validation(data) -> dict:
        """
        @param data:
        @return:
        """
        errors = user_login_schema.validate(data)
        if errors:
            print(str(errors))
            return dict(success=False, message=str(errors))

        return dict(success=True)

    @staticmethod
    def user_registration_data_validation(data) -> dict:
        """
        @param data:
        @return:
        """
        errors = user_schema.validate(data)
        if errors:
            print(str(errors))
            return dict(success=False, message=str(errors))

        return dict(success=True)


user_data_validation: UserDataValidation = UserDataValidation()
