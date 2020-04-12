from user.models import User, BlacklistToken
from app import db


class UserDAO:
    def __init__(self, model):
        """
        @param model:
        """
        self.model = model

    def get_all_users(self) -> object:
        """
        @rtype: object
        """
        return db.session.query(self.model).all()

    def get_user_by_username(self, username: str) -> object:
        """
        @param username:
        @return:
        """
        return db.session.query(self.model).filter_by(username=username).first()

    def get_user_by_id(self, user_id: int) -> object:
        """
        @param user_id:
        @return:
        """
        return db.session.query(self.model).filter_by(id=user_id).first()

    @staticmethod
    def create_user(name: str, username: str, password_hash: str) -> object:
        """
        @param name:
        @param username:
        @param password_hash:
        @return:
        """
        user: User = User(name, username, password_hash)
        db.session.add(user)
        db.session.commit()

        return user


class BlacklistTokenDAO:
    def __init__(self, model):
        """
        @param model:
        """
        self.model = model

    def get_blacklist_token(self, token: str) -> object:
        return db.session.query(self.model).filter_by(token=token).first()

    def create_blacklist_token(self, token: str) -> object:
        """
        @param token:
        @return:
        """
        token = self.model(token)
        db.session.add(token)
        db.session.commit()

        return token


user_dao: UserDAO = UserDAO(User)
blacklist_token_dao: BlacklistTokenDAO = BlacklistTokenDAO(BlacklistToken)
