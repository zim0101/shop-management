from app import db, marshmallow


# ----------------------------- Product model ------------------------------------------

class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), index=True)
    category_id = db.Column(db.Integer, nullable=False)
    subcategory_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str, category_id: int, subcategory_id: int):
        """
        @param name:
        @param category_id:
        @param subcategory_id:
        """
        self.name = name
        self.category_id = category_id
        self.subcategory_id = subcategory_id


# ----------------------------- ProductVariation model -------------------------------

class ProductVariation(db.Model):

    __tablename__ = 'product_variations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), index=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name: str, price: float, quantity: int):
        """
        @param name:
        @param price:
        @param quantity:
        """
        self.name = name
        self.price = price
        self.quantity = quantity


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


# ----------------------------- Product Schema --------------------------------------

class ProductSchema(marshmallow.Schema):

    class Meta:
        fields = ("id", "name", "category_id", "subcategory_id", "created_at")


# ----------------------------- ProductVariation Schema -----------------------------

class ProductVariationSchema(marshmallow.Schema):

    class Meta:
        fields = ("id", "name", "price", "quantity", "created_at")
