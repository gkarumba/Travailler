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

job_edit = api.model('Edits',{
    'new_title':fields.String(required=True,description='jobs title'),
    'new_category':fields.String(required=True,description='jobs category'),
    'new_responsibility':fields.String(required=True,description='jobs responsibility'),
    'new_company':fields.Integer(required=True,description='jobs company'),
    'new_location':fields.String(required=True,description='jobs location'),
    'new_salary':fields.String(required=True,description='jobs salary')
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

class EditJob(Resource):
    """
    Class with the method to edit a job
    """
    @api.expect(job_edit)
    def put(self,id):
        """
        Method to edit a job
        """
        parser = reqparse.RequestParser()
        parser.add_argument('new_title',type=str,\
                            required=True,help='new_title field cannot be empty')
        parser.add_argument('new_category',type=str,\
                            required=True,help='new_category field cannot be empty')
        parser.add_argument('new_responsibility',type=str,\
                            required=True,help='new_responsibility field cannot be empty')
        parser.add_argument('new_company',type=str,\
                            required=True,help='new_company field cannot be empty')
        parser.add_argument('new_location',type=str,\
                            required=True,help='new_location field cannot be empty')
        parser.add_argument('new_salary',type=str,\
                            required=True,help='new_salary field cannot be empty')
        args = parser.parse_args()
        
        if not validate_title(args['new_title']) or not check_space(args['new_title']):
            return abort(make_response(jsonify({'message':'Invalid new_title'}),400))
        # if not validate_category(args['new_category']) or not check_space(args['new_category']):
        #     return abort(make_response(jsonify({'message':'Invalid new_category'}),400))
        if not validate_responsibility(args['new_responsibility']) or not check_space(args['new_responsibility']):
            return abort(make_response(jsonify({'message':'Invalid new_responsibility'}),400))
        if not validate_company(args['new_company']) or not check_space(args['new_company']):
            return abort(make_response(jsonify({'message':'Invalid new_company'}),400))
        if not validate_location(args['new_location']) or not check_space(args['new_location']):
            return abort(make_response(jsonify({'message':'Invalid new_location'}),400))
        if not validate_salary(args['new_salary']):
            return abort(make_response(jsonify({'message':'Invalid new_salary'}),400))
        
        check_job = JobsModel.get_job_by_id(self,id)
        if not check_job:
            return abort(make_response(jsonify({'message':'No job found'}),400))

        response = JobsModel.change_job_details(self,title=args['new_title'],company=args['new_company'],category=args['new_category'],\
                             responsibility=args['new_responsibility'],salary=args['new_salary'],\
                             location=args['new_location'])
        if response:
            return  make_response(jsonify({"status": 200, "data": [{'message': 'job edited succesfully',
                                                                    'job':response}]}), 200)
       
class DeleteJob(Resource):
    """
    Class with method to remove a job
    """        
    def delete(self,id):
        """
        Method to remove a job
        """
        check_job = JobsModel.get_job_by_id(self,id)
        if not check_job:
            return abort(make_response(jsonify({'message':'No job found'}),400))

        response = JobsModel.delete_job(self,id)
        if response:
            return  make_response(jsonify({"status": 200, "data": [{'message': 'job deleted succesfully'
                                                                    }]}), 200)
api.add_resource(AddJob,'/jobs')
api.add_resource(GetJob,'/jobs/<int:id>')
api.add_resource(EditJob,'/jobs/edit/<int:id>')
api.add_resource(DeleteJob,'/jobs/delete/<int:id>')