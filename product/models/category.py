from app import db, marshmallow


# ------------------------------------------- Category Model ------------------------------------------
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), index=True)

    def __init__(self, name):
        """
        @param name:
        """
        self.name = name