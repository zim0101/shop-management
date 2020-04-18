from app import db
from shop.models.shop import Shop
from shop.models.shop_category import ShopCategory


class ShopDAO:
    def __init__(self, shop_model, shop_category_model):
        """
        @param shop_model:
        @param shop_category_model:
        """
        self.shop_model = shop_model
        self.shop_category_model = shop_category_model

    def get_all_shops(self) -> object:
        """
        @return: object
        """
        return db.session.query(self.shop_model) \
            .join(self.shop_category_model,
                  self.shop_category_model.id == self.shop_model.category_id) \
            .all()

    def get_shop_by_id(self, shop_id: int):
        """
        @param shop_id: int
        @return: object
        """
        return db.session.query(self.shop_model) \
            .join(self.shop_category_model,
                  self.shop_category_model.id == self.shop_model.category_id) \
            .filter_by(id=shop_id)

    def get_all_shops_by_user_id(self, user_id: int) -> object:
        """
        @param user_id: int
        @return: object
        """
        return db.session.query(self.shop_model) \
            .join(self.shop_category_model,
                  self.shop_category_model.id == self.shop_model.category_id) \
            .filter_by(user_id=user_id)

    def get_all_shops_by_category_id(self, category_id: int) -> object:
        """
        @param category_id: int
        @return: object
        """
        return db.session.query(self.shop_model) \
            .join(self.shop_category_model,
                  self.shop_category_model.id == self.shop_model.category_id) \
            .filter_by(category_id=category_id)

    def get_all_shops_by_size(self, size: int) -> object:
        """
        @param size: int
        @return: object
        """
        return db.session.query(self.shop_model) \
            .join(self.shop_category_model,
                  self.shop_category_model.id == self.shop_model.category_id) \
            .filter_by(size=size)

    def get_filtered_shops(self, filter_data: dict) -> object:
        """
        @param filter_data: object
        @return: object
        """
        shops: object = db.session.query(self.shop_model) \
            .join(self.shop_category_model,
                  self.shop_category_model.id == self.shop_model.category_id)
        if "user_id" in filter_data:
            shops.filter_by(user_id=filter_data["user_id"])
        if "category_id" in filter_data:
            shops.filter_by(category_id=filter_data["category_id"])
        if "size" in filter_data:
            shops.filter_by(size=filter_data["size"])

        return shops


shop_dao: ShopDAO = ShopDAO(Shop, ShopCategory)
