import jwt
import os
from flask import request
from functools import wraps
from werkzeug.exceptions import Unauthorized, BadRequest, NotFound
from datetime import datetime,timedelta
from app.api.v2.models.users_models import UserModel

db = UserModel()
key = os.getenv('SECRET_KEY')
class Tokens():
    """Class with methods to generate tokens and decode tokens"""
    def generate_token(self,user_id):
        """Method to generate token"""
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=60),
                'iat': datetime.utcnow(),
                'id': user_id
            }
            token = jwt.encode(payload,
                               key,
                               algorithm='HS256')
            valid_token = token.decode('utf-8')
            # print(valid_token)
            return valid_token
            
        except Exception as error:
            return str(error)

    def decode_token(self,token):
        """Method to decode token"""
        try:
            payload = jwt.decode(token,key)
        except jwt.ExpiredSignatureError:
            raise Unauthorized('Session has expired')
        except jwt.InvalidTokenError:
            raise Unauthorized('Invalid Token(jwt),Please log in')

        return payload['id']
        
tk = Tokens()
def login_required(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token_header = request.headers.get('Authorization')
        if not token_header:
            raise Unauthorized('Protected Route. Add token to access it')
        token = token_header.split(" ")[1]
        if not token:
            raise NotFound('Token missing. Please put a token')
        response = tk.decode_token(token)
        # print(response)
        if isinstance(response,str):
            raise Unauthorized('Invalid Token.Please Login(response)') 
        check_id = db.check_user_id(response)
        if not check_id:
            raise Unauthorized('Invalid Token(id).Please Login') 
        return f(*args, **kwargs)
        
    return decorator
