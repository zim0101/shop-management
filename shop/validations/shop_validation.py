from shop.schemas.shop_schema import ShopCreateSchema, ShopEditSchema


class ShopDataValidation:

    def __init__(self, shop_create_schema, shop_edit_schema):
        """
        @param shop_create_schema:
        @param shop_edit_schema:
        """
        self.shop_create_schema = shop_create_schema
        self.shop_edit_schema = shop_edit_schema

    def shop_create_data_validation(self, data) -> dict:
        """
        @param data: mapping
        @return: dict
        """
        errors = self.shop_create_schema.validate(data)
        if errors:
            print(str(errors))
            return dict(success=False, message=str(errors))

        return dict(success=True)

    def shop_edit_data_validation(self, data) -> dict:
        """
        @param data: mapping
        @return: dict
        """
        errors = self.shop_edit_schema.validate(data)
        if errors:
            print(str(errors))
            return dict(success=False, message=str(errors))

        return dict(success=True)


shop_data_validation: ShopDataValidation = ShopDataValidation(
    ShopCreateSchema,
    ShopEditSchema
)
