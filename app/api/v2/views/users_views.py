from flask_restplus import Resource,fields,reqparse\
                           ,Namespace

from flask import abort,session,make_response,jsonify

from app.api.v2.models.users_models import UserModel
from app.util.validators import validate_age,validate_education,\
                                validate_email,validate_location,\
                                validate_NationalID,validate_occupation,\
                                validate_username,check_space,check_password
from app.util.dto import AuthDto

api = AuthDto.api
_user = AuthDto.user_details

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
        print(user_exists)
        if user_exists:
            new_user = UserModel.add_user(self,username=args['username'],email=args['email'],age=args['age'],
                                  occupation=args['occupation'],education=args['education'],
                                  nationalID=args['nationalID'],location=args['location'],password=args['password'])
            return  make_response(jsonify({"status": 201, "data": [{'message': 'user succesfully created',
                                                                    'user':new_user}]}), 201)
        return abort(make_response(jsonify({'message':'User Already exists'}),400))
        
api.add_resource(UserRegistration,'/user/signup')
