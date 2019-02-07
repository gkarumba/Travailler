from flask_restplus import Namespace, fields

class UserDto():
    """Class for user DTO"""
    api = Namespace("Register",description="user related operations")

    user = api.model('Register_User',{
        "username":fields.String(required=True,description="Users username"),
        "email":fields.String(required=True,description="Users email address"),
        "password":fields.String(required=True,description="Users password"),
        "age":fields.String(required=True,description="Users age"),
        "location":fields.String(required=True,description="Users location"),
        "occupation":fields.String(required=True,description="Users occupation"),
        "education":fields.String(required=True,description="Users level of education"),
        "nationalID":fields.String(required=True,description="Users nationalID number")
    })

    login = api.model('LogIn',{
    'username':fields.String(required=True,description='Users username'),
    'password':fields.String(required=True,description='Users password')
    })


    
