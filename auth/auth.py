from flask import jsonify, request, current_app as app, Blueprint
from auth.services import user_service
from auth.validations import user_data_validation
from auth.wrappers import token_required

secret_key = app.config["SECRET_KEY"]
auth = Blueprint("auth", __name__)


@auth.route('/login', methods=['POST'])
def login() -> object:
    try:
        validator: dict = user_data_validation.user_login_data_validation(request.json)
        if not validator["success"]:
            return jsonify(validator)

        authenticate_response: dict = user_service.authenticate_user(
            request.json.get("username"),
            request.json.get("password"),
            secret_key
        )

        return jsonify(authenticate_response)
    except Exception as e:

        return jsonify({"success": False, "message": str(e)})


@auth.route('/register', methods=['POST'])
def register() -> dict:
    try:
        validator: dict = user_data_validation.user_registration_data_validation(request.json)
        if not validator["success"]:
            return jsonify(validator)

        register_user_response: dict = user_service.register_user(
            request.json.get("name"),
            request.json.get("username"),
            request.json.get("password"),
            secret_key
        )

        return jsonify(register_user_response)
    except Exception as e:

        return jsonify({"success": False, "message": str(e)})


@auth.route('/log-out', methods=['POST'])
@token_required
def logout(current_user):
    try:
        token = request.headers['Authorization']
        logout_response = user_service.logout_user(token)

        return jsonify(logout_response)
    except Exception as e:

        return jsonify({"success": False, "message": str(e)})
