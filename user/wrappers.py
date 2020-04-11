from functools import wraps
import jwt
from flask import jsonify, request, current_app as app
from user.daos import user_dao


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = user_dao.get_user_by_username(data['username'])
        except Exception as e:
            return jsonify({'message': str(e)})

        return f(current_user, *args, **kwargs)

    return decorator
