import os
from flask import Blueprint,app, request, jsonify
import validators
from .main import User,db
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from constants.http_status_codes import HTTP_200_OK,HTTP_401_UNAUTHORIZED
from flask_jwt_extended import JWTManager
auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

JWTManager(app)
JWT_SECRET_KEY=os.environ.get('jwt_secret_key')

@auth.post('/login')
def login():
    email = request.json.get('email', '')
    # password = request.json.get('password', '')

    user = User.query.filter_by(email=email).first()

    if user:
        refresh = create_refresh_token(identity=user.id)
        access = create_access_token(identity=user.id)

        return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'email': user.email
                }

            }), HTTP_200_OK

    return jsonify({'error': 'This email id is not registered. Please contact admin.'}), HTTP_401_UNAUTHORIZED