from app import db


# ------------------------------------------- User Model ------------------------------------------
class Category(db.Model):
    """
        Shop Model
    """
    __tablename__ = 'shop_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str):
        """
        @param name: str
        """
        self.name = name
