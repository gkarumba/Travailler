from flask_restplus import Resource,fields,reqparse\
                           ,Namespace

from flask import abort,session,make_response,jsonify
from app.util.tokens import Tokens
from app.api.v2.models.users_models import UserModel
from app.util.validators import validate_age,validate_education,\
                                validate_email,validate_location,\
                                validate_NationalID,validate_occupation,\
                                validate_username,check_space,check_password
from app.util.dto import AuthDto

tk = Tokens()
db = UserModel()
api = AuthDto.api
_user = AuthDto.user_details
_login = AuthDto.login_details

# db = UserModel()
class UserRegistration(Resource):
    """
    Class with the methods to register a new user
    """
    @api.expect(_user, validate=True)
    # @api.route('/user/signup')
    def post(self):
        """
        Method to add a new user
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,\
                            required=True,help='username field cannot be empty')
        parser.add_argument('email',type=str,\
                            required=True,help='Email field cannot be empty')
        parser.add_argument('password',type=str,\
                            required=True,help='password field cannot be empty')
        parser.add_argument('age',type=int,\
                            required=True,help='Age field cannot be empty')
        parser.add_argument('location',type=str,\
                            required=True,help='Location field cannot be empty')
        parser.add_argument('occupation',type=str,\
                            required=True,help='occupation field cannot be empty')
        parser.add_argument('education',type=str,\
                            required=True,help='education field cannot be empty')
        parser.add_argument('nationalID',type=int,\
                            required=True,help='nationalID field cannot be empty')
        args = parser.parse_args(strict=True)
        
        if not validate_username(args['username']) or not check_space(args['username']):
            return abort(make_response(jsonify({'message':'Invalid username'}),400))
        if not validate_email(args['email']):
            return abort(make_response(jsonify({'message':'Invalid Email'}),400))
        if not check_password(args['password']):
            return abort(make_response(jsonify({'message':'Invalid Password,atleast 8 characters'}),400))
        if not validate_age(args['age']):
            return abort(make_response(jsonify({'message':'Invalid age'}),400))
        if not validate_occupation(args['occupation']):
            return abort(make_response(jsonify({'message':'Invalid occupation'}),400))
        if not validate_education(args['education']):
            return abort(make_response(jsonify({'message':'Invalid education'}),400))
        if not validate_NationalID(args['nationalID']):
            return abort(make_response(jsonify({'message':'Invalid nationalID'}),400))
        if not validate_location(args['location']):
            return abort(make_response(jsonify({'message':'Invalid location'}),400))
        
        user_exists = UserModel.check_user_exists(self,args['nationalID'])
        # print(user_exists)
        if user_exists:
            new_user = UserModel.add_user(self,username=args['username'],email=args['email'],age=args['age'],
                                  occupation=args['occupation'],education=args['education'],
                                  nationalID=args['nationalID'],location=args['location'],password=args['password'])
            if new_user:
                set_admin = UserModel.set_role(self,new_user)
                if not set_admin:
                    return make_response(jsonify({"status": 201, "data": [{'message': 'user succesfully created',
                                                                  'role':'Not Admin','user':new_user}]}), 201)
                return  make_response(jsonify({"status": 201, "data": [{'message': 'user succesfully created',
                                                                 'role':'Admin','user':new_user}]}), 201)
        return abort(make_response(jsonify({'message':'User Already exists'}),400))
        
api.add_resource(UserRegistration,'/user/signup')

class SignIn(Resource):
    """Class with methods to allow user to login"""
    @api.expect(_login)
    def post(self):
        """Method to allow user to login"""
        parser = reqparse.RequestParser()
        parser.add_argument('nationalID',type=int,\
                            required=True,help='nationalID field cannot be empty')
        parser.add_argument('password',type=str,\
                            required=True,help='password field cannot be empty')
        args = parser.parse_args(strict=True)

        if not validate_NationalID(args['nationalID']):
            return abort(make_response(jsonify({'message':'Invalid nationalID'}),400))
        if not check_password(args['password']):
            return abort(make_response(jsonify({'message':'Invalid Password,atleast 8 characters'}),400))
        
        user_exists = db.check_user_exists(args['nationalID'])
        if not user_exists:
            user_login = db.match_password(args['password'],args['nationalID'])
            if user_login:
                user_id = db.get_user_id(args['nationalID'])
                # print(user_id)
                if not user_id:
                    return abort(make_response(jsonify({'message':'No User Found'}),400))
                token = tk.generate_token(user_id)
                return make_response(jsonify({"status": 200, "data": [{'message': 'user succesfully logged in',
                                                                    'token':token}]}), 200)
        return abort(make_response(jsonify({'message':'No User Found'}),400))

api.add_resource(SignIn,'/user/signin')
