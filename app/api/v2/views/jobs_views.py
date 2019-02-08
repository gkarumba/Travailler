from flask_restplus import Resource,fields,reqparse\
                           ,Namespace
from flask import abort,session,make_response,jsonify

from app.util.tokens import *
from app.api.v2.models.jobs_models import JobModels
from app.util.validators import validate_title,validate_responsibility,\
                                validate_company,validate_location,\
                                validate_category,validate_salary,\
                                check_space
from app.util.dto import JobsDto

api = JobsDto.api
_jobs = JobsDto.jobs
_edits = JobsDto.job_edits
tk = Tokens()
db = JobModels()

class PostJob(Resource):
    """
    Class with methods to add/retrieve books
    """
    @login_required
    @api.expect(_jobs)
    def post(self):
        """
        Method to add a book
        """
        parser = reqparse.RequestParser()
        parser.add_argument('title',type=str,\
                            required=True,help='title field cannot be empty')
        parser.add_argument('category',type=str,\
                            required=True,help='category field cannot be empty')
        parser.add_argument('responsibility',type=str,\
                            required=True,help='responsibility field cannot be empty')
        parser.add_argument('company',type=str,\
                            required=True,help='company field cannot be empty')
        parser.add_argument('location',type=str,\
                            required=True,help='Location field cannot be empty')
        parser.add_argument('salary',type=str,\
                            required=True,help='salary field cannot be empty')
        args = parser.parse_args()
        
        if not validate_title(args['title']) or not check_space(args['title']):
            return abort(make_response(jsonify({'message':'Invalid title'}),400))
        if not validate_category(args['category']) or not check_space(args['category']):
            return abort(make_response(jsonify({'message':'Invalid category'}),400))
        if not validate_responsibility(args['responsibility']) or not check_space(args['responsibility']):
            return abort(make_response(jsonify({'message':'Invalid responsibility'}),400))
        if not validate_company(args['company']) or not check_space(args['company']):
            return abort(make_response(jsonify({'message':'Invalid company'}),400))
        if not validate_location(args['location']) or not check_space(args['location']):
            return abort(make_response(jsonify({'message':'Invalid location'}),400))
        if not validate_salary(args['salary']):
            return abort(make_response(jsonify({'message':'Invalid salary'}),400))

        job_exists = db.check_job_exists(args['title'])
        if not job_exists:
            return make_response(jsonify({'message':'job already exists',}),400)
        new_job = db.add_job(title=args['title'],company=args['company'],category=args['category'],\
                             responsibility=args['responsibility'],salary=args['salary'],\
                             location=args['location'])
        if new_job:    
            return  make_response(jsonify({"status": 201, "data": [{'message': 'job succesfully added',
                                                                    'ID':new_job['job_id']}]}), 201)

api.add_resource(PostJob,'/jobs')