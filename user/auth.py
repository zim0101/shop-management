from flask import jsonify, request, make_response, current_app as app
from user.services import user_service
from user.schemas import UserSchema, UserLoginSchema
from user.wrappers import token_required

user_login_schema = UserLoginSchema()
user_schema = UserSchema()


@app.route('/login', methods=['POST'])
def login() -> object:
    errors = user_login_schema.validate(request.json)
    if errors:
        return jsonify({
            "success": False,
            "message": str(errors)
        })

    username: str = request.json.get("username")
    password: str = request.json.get("password")
    secret_key: str = app.config["SECRET_KEY"]
    authenticate_response: dict = user_service.authenticate_user(username, password, secret_key)
    if authenticate_response["success"]:
        return jsonify({
            "success": True,
            "username": authenticate_response["username"],
            "token": authenticate_response["token"]
        })

    return make_response('Authentication failed', 401, {
        'WWW-Authenticate': 'Basic-realm="Login required"'
    })


@app.route('/register', methods=['POST'])
def register() -> dict:
    errors = user_schema.validate(request.json)
    if errors:
        return jsonify({
            "success": False,
            "message": str(errors)
        })

    name: str = request.json.get("name")
    username: str = request.json.get("username")
    password: str = request.json.get("password")
    secret_key: str = app.config["SECRET_KEY"]

    register_user_response: dict = user_service.register_user(name, username, password, secret_key)
    if register_user_response["success"]:
        return jsonify({
            "success": True,
            "username": register_user_response["username"],
            "token": register_user_response["token"],
            "message": "User registration successful"
        })

    return jsonify({
        "success": False,
        "message": "User registration failed"
    })


@app.route('/user-details', methods=['GET'])
@token_required
def user_details(current_user):
    print(current_user)
    pass
