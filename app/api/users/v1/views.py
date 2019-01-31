from flask_restplus import Resource,fields,reqparse\
                           ,Namespace

from flask import abort,session,make_response,jsonify

from app.api.users.v1.models import UserModels,users
from app.util.validators import validate_age,validate_education,\
                                validate_email,validate_location,\
                                validate_NationalID,validate_occupation,\
                                validate_username,check_space

api = Namespace('Users',description='user related operations')

user = api.model('Users',{
    'username':fields.String(required=True,description='Users username'),
    'email':fields.String(required=True,description='Users email address'),
    'age':fields.Integer(required=True,description='Users age'),
    'location':fields.String(required=True,description='Users location'),
    'occupation':fields.String(required=True,description='Users occupation'),
    'education':fields.String(required=True,description='Users level of education'),
    'NationalID':fields.Integer(required=True,description='Users NationalID number')
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
        if not user_exists:
            new_user = UserModels(username=args['username'],email=args['email'],age=args['age'],
                                  occupation=args['occupation'],education=args['education'],
                                  NationalID=args['NationalID'],location=args['location'])
            register = users.append(new_user)
            return  make_response(jsonify({"status": 201, "data": [{'message': 'user succesfully created',
                                                                    'user':new_user.serialize()}]}), 201)
        return abort(make_response(jsonify({'message':'User Already exists'}),400))

api.add_resource(Registration,'/user/register')