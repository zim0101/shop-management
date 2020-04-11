import jwt
import datetime
from user.daos import user_dao
from app import bcrypt


class UserService:

    @staticmethod
    def user_exist(username: str, password: str) -> bool:
        """
        @param username:
        @param password:
        @return:
        """
        user = user_dao.get_user_by_username(username)
        if user and bcrypt.check_password_hash(user.password, password):
            return True

        return False

    @staticmethod
    def generate_api_token(username: str, secret_key: str) -> dict:
        """
        @param username:
        @param secret_key:
        @return:
        """
        try:
            token_life_time: datetime = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            payload: dict = dict(user=username, exp=token_life_time)
            token: bytes = jwt.encode(payload, secret_key)

            return dict(success=True, token=token.decode('UTF-8'))
        except Exception as e:

            return dict(success=False, message=e)

    def authenticate_user(self, username: str, password: str, secret_key: str) -> dict:
        """
        @param username:
        @param password:
        @param secret_key:
        @return:
        """
        if self.user_exist(username, password):
            generate_token_response: dict = self.generate_api_token(username, secret_key)
            return dict(success=True, username=username, token=generate_token_response["token"])
        return dict(success=False)

    def register_user(self, name: str, username: str, password: str, secret_key: str) -> dict:
        """
        @param name:
        @param username:
        @param password:
        @param secret_key:
        @return:
        """
        password_hash = bcrypt.generate_password_hash(password)
        user = user_dao.create_user(name, username, password_hash)
        if user:
            generate_token_response: dict = self.generate_api_token(username, secret_key)
            return dict(success=True, username=username, token=generate_token_response["token"])

        return dict(success=False)


user_service: UserService = UserService()
