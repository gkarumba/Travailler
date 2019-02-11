from flask_restplus import Resource,fields,reqparse\
                           ,Namespace
from flask import abort,make_response,jsonify

from app.util.tokens import *
from app.api.v2.models.jobs_models import JobModels
from app.util.validators import validate_title,validate_responsibility,\
                                validate_company,validate_location,\
                                validate_category,validate_salary,\
                                check_space,validate_status
from app.util.dto import JobsDto

api = JobsDto.api
_jobs = JobsDto.jobs
_edits = JobsDto.job_edits
_apply = JobsDto.job_apply
tk = Tokens()
db = JobModels()
gti = GetUserId()

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
    @login_required
    def get(self):
        """Method to retrieve all jobs"""
        response = db.get_all_jobs()
        if response:
            return  make_response(jsonify({"status": 200, "data": [{'message': 'jobs available',
                                                                    'jobs':response}]}), 200)
        return abort(make_response(jsonify({'message':'No jobs Found'}),400))
api.add_resource(PostJob,'/jobs')

class GetJob(Resource):
    """Class with method to get one job"""
    def get(self,id):
        """Method to get one job"""
        response = db.get_one(id)
        if response:
            return  make_response(jsonify({"status": 200, "data": [{'message': 'jobs available',
                                                                    'jobs':response}]}), 200)
        return abort(make_response(jsonify({'message':'No jobs Found'}),400))

api.add_resource(GetJob,'/jobs/<int:id>')

class EditJob(Resource):
    """Class with method to edit job"""
    @login_required
    @api.expect(_edits)
    def put(self,id):
        """Method to edit job"""
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
        if not validate_category(args['new_category']) or not check_space(args['new_category']):
            return abort(make_response(jsonify({'message':'Invalid new_category'}),400))
        if not validate_responsibility(args['new_responsibility']) or not check_space(args['new_responsibility']):
            return abort(make_response(jsonify({'message':'Invalid new_responsibility'}),400))
        if not validate_company(args['new_company']) or not check_space(args['new_company']):
            return abort(make_response(jsonify({'message':'Invalid new_company'}),400))
        if not validate_location(args['new_location']) or not check_space(args['new_location']):
            return abort(make_response(jsonify({'message':'Invalid new_location'}),400))
        if not validate_salary(args['new_salary']):
            return abort(make_response(jsonify({'message':'Invalid new_salary'}),400))
        
        check_job = db.get_job_by_id(id)
        # print(check_job)
        if not check_job:
            return abort(make_response(jsonify({'message':'No job found'}),400))
        new_job = { 'title':args['new_title'],
                    'company':args['new_company'],
                    'category':args['new_category'],
                    'responsibility':args['new_responsibility'],
                    'salary':args['new_salary'],
                    'location':args['new_location']
        }
        shared_items = {k: check_job[k] for k in check_job if k in new_job and check_job[k] == new_job[k]}
        # print(shared_items)
        if not shared_items:
            # return abort(make_response(jsonify({'message':'No edit required'}),400))
        # print(new_job)
        # if new_job == check_job:
        #     return abort(make_response(jsonify({'message':'No edit required'}),400))

            response = db.edit_job_details(id,title=args['new_title'],company=args['new_company'],category=args['new_category'],\
                                responsibility=args['new_responsibility'],salary=args['new_salary'],\
                                location=args['new_location'])
            if response:
                return  make_response(jsonify({"status": 200, "data": [{'message': 'job edited succesfully',
                                                                        'job':response}]}), 200)
            return abort(make_response(jsonify({'message':'No job found'}),400))
        return abort(make_response(jsonify({'message':'No editing required'}),400))

api.add_resource(EditJob,'/jobs/edit/<int:id>')

class DeleteJob(Resource):
    """Class with method to delete a job"""
    @login_required
    def delete(self,id):
        """Methods to delete a job"""
        response = db.delete_jobs(id)
        # print(response)
        if response == None:
            return  make_response(jsonify({"status": 200, "data": [{'message': 'job deleted succesfully'
                                                                        }]}), 200)
        return abort(make_response(jsonify({'message':'No job found'}),400))
api.add_resource(DeleteJob,'/jobs/delete/<int:id>')

class ApplyJob(Resource):
    """Class with method to apply for a job"""
    @login_required
    @api.expect(_apply)
    def post(self,id):
        """Method to apply for a job"""
        user_id = gti.user_creds()
        # print(user_id)
        parser = reqparse.RequestParser()
        parser.add_argument('status',type=str,\
                            required=True,help='status field cannot be empty')
        args = parser.parse_args()

        if not validate_status(args['status']):
            return abort(make_response(jsonify({'message':'Invalid status'}),400))

        check_job = db.get_job_by_id(id)
        if not check_job:
            return abort(make_response(jsonify({'message':'No job found'}),400))
        apply_job = db.apply_job(id,args['status'],user_id)
        # print(apply_job)
        if apply_job:
            return  make_response(jsonify({"status": 200, "data": [{'message': 'job application succesfully',
                                                                    'appliction':apply_job}]}), 200)
        return abort(make_response(jsonify({'message':'No application unsuccessful'}),400))
api.add_resource(ApplyJob,'/jobs/apply/<int:id>')
                                                                



