from flask import Blueprint, jsonify
from product.models.product import Product, ProductSchema

product = Blueprint("product", __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@product.route('/all-products')
def products():
    try:
        products_query = Product.query.all()
        all_product = products_schema.dump(products_query)
        data = [
            {
                'success': True,
                'status': 200,
                'products': all_product
            }
        ]

        return jsonify(data)
    except Exception as e:
        result = {'success': False}
        print(e)

        return jsonify(result)
