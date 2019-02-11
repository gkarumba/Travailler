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

class AuthDto():
    """Class for user DTO"""
    api = Namespace("Register_User",description="user related operations")

    user_details = api.model('signUp_User',{
        "username":fields.String(required=True,description="Users username"),
        "email":fields.String(required=True,description="Users email address"),
        "password":fields.String(required=True,description="Users password"),
        "age":fields.String(required=True,description="Users age"),
        "location":fields.String(required=True,description="Users location"),
        "occupation":fields.String(required=True,description="Users occupation"),
        "education":fields.String(required=True,description="Users level of education"),
        "nationalID":fields.String(required=True,description="Users nationalID number")
    })

    login_details = api.model('LogIn',{
    'nationalID':fields.String(required=True,description='Users nationalID'),
    'password':fields.String(required=True,description='Users password')
    })

class JobsDto():
    """Class for jobs DTO"""
    api = Namespace('Jobs_v2',description='Job related operations')

    jobs = api.model('Jobs_v2',{
        'title':fields.String(required=True,description='jobs title'),
        'category':fields.String(required=True,description='jobs category'),
        'responsibility':fields.String(required=True,description='jobs responsibility'),
        'company':fields.Integer(required=True,description='jobs company'),
        'location':fields.String(required=True,description='jobs location'),
        'salary':fields.String(required=True,description='jobs salary')
    })

    job_edits = api.model('Edits',{
        'new_title':fields.String(required=True,description='jobs title'),
        'new_category':fields.String(required=True,description='jobs category'),
        'new_responsibility':fields.String(required=True,description='jobs responsibility'),
        'new_company':fields.Integer(required=True,description='jobs company'),
        'new_location':fields.String(required=True,description='jobs location'),
        'new_salary':fields.String(required=True,description='jobs salary')
    })

    job_apply = api.model('Apply',{
        'status':fields.String(required=True,description='application status')
    })
    