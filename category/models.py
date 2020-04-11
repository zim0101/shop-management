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


# ------------------------------------------- Subcategory Model ------------------------------------------

class Subcategory(db.Model):
    
    __tablename__ = 'subcategories'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), index=True)
    category_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, category_id: int):
        """
        @param name:
        @param category_id:
        """
        self.name = name
        self.category_id = category_id


# ------------------------------------------- Category Schema ------------------------------------------

class CategorySchema(marshmallow.Schema):
    
    class Meta:
        fields = ("id", "name")


# ------------------------------------------- Subcategory Schema ------------------------------------------

class SubcategorySchema(marshmallow.Schema):
    
    class Meta:
        fields = ("id", "name", "category_id")
