from flask import Blueprint, jsonify, request
from app.utils import crypto
from shop.services.shop_service import shop_service
from shop.validations.shop_validation import shop_data_validation

shop = Blueprint("shop", __name__)


@shop.route('/all-shops', method=["GET"])
def all_shops():
    try:
        shops = shop_service.all_shops()
    except Exception as e:

        return jsonify(dict(success=False, message=str(e)))

    return jsonify(shops)


@shop.route('/shops-by-user', method=["GET"])
def shops_by_user():
    try:
        shops = shop_service.get_shops_of_user(request.json.get("user_id"))
    except Exception as e:

        return jsonify(dict(success=False, message=str(e)))

    return jsonify(shops)


@shop.route('/filter-shops', method=["GET"])
def filter_shops():
    pass


@shop.route('/shop-details', method=["GET"])
def shop_details():
    try:
        decrypted_id = crypto.decrypt_id(request.json.get("shop_id"))
        shop_data = shop_service.shop_details(decrypted_id)
    except Exception as e:

        return jsonify(dict(success=False, message=str(e)))

    return jsonify(shop_data)


@shop.route('/create-shop', method=["POST"])
def create_shop():
    try:
        validation_response = shop_data_validation.shop_create_schema(
            request.json)
        if not validation_response["success"]:
            return validation_response

        response = shop_service.store_shop(
            request.json.get("name"),
            request.json.get("user_id"),
            request.json.get("category_id"),
            request.json.get("address"),
            request.json.get("size")
        )
    except Exception as e:

        return jsonify(dict(success=False, message=str(e)))

    return jsonify(response)


@shop.route('/edit-shop', method=["POST"])
def edit_shops():
    try:
        validation_response = shop_data_validation.shop_edit_data_validation(
            request.json)
        if not validation_response["success"]:
            return validation_response

        response = shop_service.update_shop(
            request.json.get("shop_id"),
            request.json.get("name"),
            request.json.get("user_id"),
            request.json.get("category_id"),
            request.json.get("address"),
            request.json.get("size")
        )
    except Exception as e:

        return jsonify(dict(success=False, message=str(e)))

    return jsonify(response)
