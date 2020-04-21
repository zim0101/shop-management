from app import db
from shop.models.shop_category import ShopCategory


class ShopCategoryDAO:
    def __init__(self, shop_category_model):
        """
        @param shop_category_model:
        """
        self.shop_category_model = shop_category_model

    def get_all_categories(self) -> object:
        """
        @return: object
        """
        return db.session.query(self.shop_category_model).all()

    def get_category_by_id(self, category_id: int) -> object:
        """
        @param category_id: int
        @return: object
        """
        return db.session.query(self.shop_category_model) \
            .filter_by(id=category_id)

    def store_category(self, name: str) -> object:
        """
        @param name: str
        @return: object
        """
        category = self.shop_category_model(name)
        db.session.commit(category)

        return category

    def update_category(self, category_id: int, name: str = None) -> object:
        """
        @param category_id: int
        @param name: str
        @return: object
        """
        category = self.get_category_by_id(category_id)
        category.name = name if name is not None else category.name

        return category


shop_category_dao: ShopCategoryDAO = ShopCategoryDAO(ShopCategory)
