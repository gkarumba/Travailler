from flask_restplus import Resource,fields,reqparse\
                           ,Namespace

from flask import abort,session,make_response,jsonify

from app.api.users.v1.models import UserModels,users
from app.util.validators import validate_age,validate_education,\
                                validate_email,validate_location,\
                                validate_NationalID,validate_occupation,\
                                validate_username,check_space,check_password

api = Namespace('Users',description='user related operations')

user = api.model('Register',{
    'username':fields.String(required=True,description='Users username'),
    'email':fields.String(required=True,description='Users email address'),
    'password':fields.String(required=True,description='Users password'),
    'age':fields.Integer(required=True,description='Users age'),
    'location':fields.String(required=True,description='Users location'),
    'occupation':fields.String(required=True,description='Users occupation'),
    'education':fields.String(required=True,description='Users level of education'),
    'NationalID':fields.Integer(required=True,description='Users NationalID number')
})

api = Namespace('LogIn',description='user related operations')

login = api.model('LogIn',{
    'username':fields.String(required=True,description='Users username'),
    'password':fields.String(required=True,description='Users password')
    })

class Registration(Resource):
    """
    Class with the methods to register a new user
    """
    @api.expect(user)
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
        parser.add_argument('NationalID',type=int,\
                            required=True,help='NationalID field cannot be empty')
        args = parser.parse_args()
        
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
        if not validate_NationalID(args['NationalID']):
            return abort(make_response(jsonify({'message':'Invalid nationaId'}),400))
        if not validate_location(args['location']):
            return abort(make_response(jsonify({'message':'Invalid location'}),400))
        
        user_exists = UserModels.check_id_number(self,args['NationalID'])
        # print(user_exists)
        if not user_exists:
            new_user = UserModels(username=args['username'],email=args['email'],age=args['age'],
                                  occupation=args['occupation'],education=args['education'],
                                  NationalID=args['NationalID'],location=args['location'],password=args['password'])
            register = users.append(new_user)
            return  make_response(jsonify({"status": 201, "data": [{'message': 'user succesfully created',
                                                                    'user':new_user.serialize()}]}), 201)
        return abort(make_response(jsonify({'message':'User Already exists'}),400))

class Login(Resource):
    """
    Class with method to login
    """
    @api.expect(login)
    def post(self):
        """
        Method to login user
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,\
                            required=True,help='username field cannot be empty')
        parser.add_argument('password',type=str,\
                            required=True,help='password field cannot be empty')
        args = parser.parse_args()

        if not validate_username(args['username']) or not check_space(args['username']):
            return abort(make_response(jsonify({'message':'Invalid username'}),400))
        if not check_password(args['password']):
            return abort(make_response(jsonify({'message':'Invalid Password,atleast 8 characters'}),400))
        
        username_exists = UserModels.validate_username(self,args['username'])
        if username_exists:
            user_password = UserModels.validate_password(self,args['password'])
            if user_password:
                return  make_response(jsonify({"status": 200, "data": [{'message': 'user succesfully logged in',
                                                                    }]}), 200)
            return abort(make_response(jsonify({'message':'Invalid Password Try Again'}),400))
        return abort(make_response(jsonify({'message':'Invalid Username Try Again'}),400))

api.add_resource(Registration,'/user/register')
api.add_resource(Login,'/user/login')