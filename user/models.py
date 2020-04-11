from app import db
from app.constants import EMAIL_VERIFIED_FALSE, USER_ROLE_SHOPKEEPER


# ------------------------------------------- User Model ------------------------------------------

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Integer, nullable=False, default=USER_ROLE_SHOPKEEPER)
    email_verified = db.Column(db.Integer, nullable=False, default=EMAIL_VERIFIED_FALSE)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str, username: str, password: str):
        """
        @param name:
        @param username:
        @param password:
        """
        self.name = name
        self.username = username
        self.password = password
