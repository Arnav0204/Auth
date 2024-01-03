from datetime import datetime, timedelta
from Auth.settings import JWT_CONF,SECRET_KEY
from jose import jwt
from django.conf import settings
# from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError
from django.contrib.auth.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    
    @classmethod
    def create_jwt(cls, user):
        # Create the JWT payload
        payload = {
            'id': user.id,
            'email': user.email,
            'exp': int((datetime.now() + timedelta(hours=JWT_CONF['TOKEN_LIFETIME_HOURS'])).timestamp()),
            # set the expiration time for 5 hour from now
            'iat': datetime.now().timestamp(),
            'username': user.username,
        }

        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jwt_token


    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token