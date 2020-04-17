from shop.schemas.shop_category_schema import ShopCategoryCreateSchema, ShopCategoryEditSchema


class ShopCategoryDataValidation:

    def __init__(self, shop_category_create_schema, shop_category_edit_schema):
        """
        @param shop_category_create_schema:
        @param shop_category_edit_schema:
        """
        self.shop_category_create_schema = shop_category_create_schema
        self.shop_category_edit_schema = shop_category_edit_schema

    def shop_category_create_data_validation(self, data) -> dict:
        """
        @param data: mapping
        @return: dict
        """
        errors = self.shop_category_create_schema.validate(data)
        if errors:
            print(str(errors))
            return dict(success=False, message=str(errors))

        return dict(success=True)

    def shop_category_edit_data_validation(self, data) -> dict:
        """
        @param data: mapping
        @return: dict
        """
        errors = self.shop_category_edit_schema.validate(data)
        if errors:
            print(str(errors))
            return dict(success=False, message=str(errors))

        return dict(success=True)


shop_category_data_validation: ShopCategoryDataValidation = ShopCategoryDataValidation(ShopCategoryCreateSchema,
                                                                                       ShopCategoryEditSchema)
