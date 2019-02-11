import jwt
import os
from functools import wraps
from werkzeug.exceptions import Unauthorized, BadRequest, NotFound
from datetime import datetime,timedelta
from app.api.v2.models.users_models import UserModel

db = UserModel()

class Tokens():
    """Class with methods to generate tokens and decode tokens"""
    def generate_token(self,user_id):
        """Method to generate token"""
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow(),
                'id': user_id
            }
            token = jwt.encode(payload,
                               key = os.getenv('SECRET_KEY'),
                               algorithm='HS256')
            valid_token = token.decode('utf-8')
            return valid_token
            
        except Exception as error:
            return str(error)

    def decode_token(self,token):
        """Method to decode token"""
        try:
            payload = jwt.decode(auth_token,key)
        except jwt.ExpiredSignatureError:
            raise Unauthorized('Session has expired')
        except jwt.InvalidTokenError:
            raise Unauthorized('Invalid Token,Please log in')

        return payload['id']

def login_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token_header = request.headers.get('Authorization')
        if not token_header:
            raise Unauthorized('Protected Route. Add token to access it')
        token_auth = token_header.split(" ")[1]
        if not token_auth:
            raise NotFound('Token missing. Please put a token')
        response = Tokens.decode_token(token_auth)
        if isinstance(response,str):
            check_id = db.check_user_id(response)
            if not check_id:
                raise Unauthorized('Invalid Token.Please Login') 
            return f(*args, **kwargs)
        raise Unauthorized('Invalid Token.Please Login') 
    return decorator

