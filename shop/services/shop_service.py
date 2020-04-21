from shop.daos.shop_dao import shop_dao


class ShopService:
    def __init__(self, dao):
        """
        @param dao:
        """
        self.dao = dao

    def shop_details(self, shop_id: int) -> dict:
        """
        @param shop_id: int
        @return: dict
        """
        shop = self.dao.get_shop_by_id(shop_id)
        if shop is None:
            return dict(success=False, message="Shop not found")

        return dict(success=True, data=shop)

    def all_shops(self) -> object:
        """
        @return: object
        """
        shops = self.dao.get_all_shops()
        if shops is None:
            return dict(success=False, message="Something went wrong")

        return dict(success=True, data=shops)

    def get_shops_of_user(self, user_id: int) -> dict:
        shops = self.dao.get_all_shops_by_user_id(user_id)
        if shops is None:
            return dict(success=False, message="Something went wrong")

        return dict(success=True, data=shops)

    def store_shop(self, name: str, user_id: int, category_id: int,
                   address: str, size: int) -> dict:
        """
        @param name: str
        @param user_id: int
        @param category_id: int
        @param address: str
        @param size: int
        @return: dict
        """
        shop = self.dao.store_shop(name, user_id, category_id, address, size)

        return dict(success=True, shop=shop)

    def update_shop(self, shop_id: int, name: str = None,
                    user_id: int = None, category_id: int = None,
                    address: str = None, size: int = None) -> dict:
        """
        @param shop_id: int
        @param name: str
        @param user_id: int
        @param category_id: int
        @param address: str
        @param size: int
        @return: dict
        """
        shop = self.dao.update_shop(
            shop_id,
            name,
            user_id,
            category_id,
            address,
            size
        )

        return dict(success=True, shop=shop)


shop_service: ShopService = ShopService(shop_dao)
