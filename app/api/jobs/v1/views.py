from flask_restplus import Resource,fields,reqparse\
                           ,Namespace
import json
from flask import abort,session,make_response,jsonify
from app.api.jobs.v1.models import JobsModel,jobs
from app.util.validators import validate_company,validate_location,\
                                validate_responsibility,validate_salary,\
                                validate_title,check_space

db = JobsModel()

api = Namespace('Jobs',description='Job related operations')

job = api.model('Jobs',{
    'title':fields.String(required=True,description='jobs title'),
    'category':fields.String(required=True,description='jobs category'),
    'responsibility':fields.String(required=True,description='jobs responsibility'),
    'company':fields.Integer(required=True,description='jobs company'),
    'location':fields.String(required=True,description='jobs location'),
    'salary':fields.String(required=True,description='jobs salary')
})

class AddJob(Resource):
    """
    Class with methods to add/retrieve books
    """
    @api.expect(job)
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
        # if not validate_category(args['category']) or not check_space(args['category']):
        #     return abort(make_response(jsonify({'message':'Invalid category'}),400))
        if not validate_responsibility(args['responsibility']) or not check_space(args['responsibility']):
            return abort(make_response(jsonify({'message':'Invalid responsibility'}),400))
        if not validate_company(args['company']) or not check_space(args['company']):
            return abort(make_response(jsonify({'message':'Invalid company'}),400))
        if not validate_location(args['location']) or not check_space(args['location']):
            return abort(make_response(jsonify({'message':'Invalid location'}),400))
        if not validate_salary(args['salary']):
            return abort(make_response(jsonify({'message':'Invalid salary'}),400))

        new_job = db.add_job(title=args['title'],company=args['company'],category=args['category'],\
                             responsibility=args['responsibility'],salary=args['salary'],\
                             location=args['location'])
        if new_job == 'job already exists':
            return make_response(jsonify({'message':'job already exists',}),400)
        return  make_response(jsonify({"status": 201, "data": [{'message': 'job succesfully added',
                                                                    'job':new_job['jobid']}]}), 201)

    def get(self):
        """
        Method to retrieve all jobs
        """
        get_jobs = JobsModel.get_all(self)
        if get_jobs:
            # myJson = json.dumps([x.__dict__ for x in get_jobs])
            return  make_response(jsonify({"status": 200, "data": [{'message': 'jobs available',
                                                                    'job':get_jobs}]}), 200)
        return abort(make_response(jsonify({'message':'No job found'}),400))

class GetJob(Resource):
    """
    Class with methods to get a book
    """
    def get(self,id):
        """
        method to get a book
        """
        get_job = JobsModel.get_one(self,id)
        if get_job:
            return  make_response(jsonify({"status": 200, "data": [{'message': 'jobs available',
                                                                    'job':get_job}]}), 200)
        return abort(make_response(jsonify({'message':'No job found'}),400))

api.add_resource(AddJob,'/jobs')
api.add_resource(GetJob,'/jobs/<int:id>')