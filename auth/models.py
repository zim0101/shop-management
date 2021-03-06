import datetime
from app import db
from app.constants import EMAIL_VERIFIED_FALSE, USER_ROLE_SHOPKEEPER


class User(db.Model):
    """
        User Model
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=USER_ROLE_SHOPKEEPER)
    email_verified = db.Column(db.Integer, nullable=False,
                               default=EMAIL_VERIFIED_FALSE)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),
                           server_onupdate=db.func.now())

    def __init__(self, name: str, username: str, password: str):
        """
        @param name:
        @param username:
        @param password:
        """
        self.name = name
        self.username = username
        self.password = password


class BlacklistToken(db.Model):
    """
    Blacklisted Token Model for storing Blacklisted JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        """
        @param token:
        """
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        """
        @return:
        """
        return '<id: token: {}'.format(self.token)
