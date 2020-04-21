from app import db
from app.constants import SHOP_TYPE_SMALL


class Shop(db.Model):
    """
        Shop Model
    """
    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    size = db.Column(db.SmallInteger, default=SHOP_TYPE_SMALL, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(),
                           server_onupdate=db.func.now())

    def __init__(self, name: str, user_id: int, category_id: int, address: str,
                 size: int):
        """
        @param name: str
        @param user_id: int
        @param category_id: int
        @param address: str
        @param size: int
        """
        self.name = name
        self.user_id = user_id
        self.category_id = category_id
        self.address = address
        self.size = size
