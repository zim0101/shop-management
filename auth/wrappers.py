from functools import wraps
import jwt
from flask import jsonify, request, current_app as app
from auth.daos import user_dao
from auth.services import blacklist_token_service


def token_required(f):
    """
    @param f:
    @return:
    """
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'message': 'Invalid Token'})

        if blacklist_token_service.in_blacklist(token):
            return jsonify({'message': 'Token is in blacklist'})

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = user_dao.get_user_by_username(data['username'])
        except Exception as e:
            return jsonify({'message': str(e)})

        return f(current_user, *args, **kwargs)

    return decorator
