from flask_restplus import Resource,fields,reqparse\
                           ,Namespace

from flask import abort,session,make_response,jsonify
from app.api.jobs.v1.models import JobsModel,jobs
from app.util.validators import validate_company,validate_location,\
                                validate_responsibility,validate_salary,\
                                validate_title,check_space

api = Namespace('Jobs',description='Job related operations')

job = api.model('Jobs',{
    'title':fields.String(required=True,description='jobs title'),
    'category':fields.String(required=True,description='jobs category'),
    'responsibility':fields.String(required=True,description='jobs responsibility'),
    'company':fields.Integer(required=True,description='jobs company'),
    'location':fields.String(required=True,description='jobs location'),
    'salary':fields.String(required=True,description='jobs occupation')
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

        job_exists = JobsModel.check_job_title(self,args['title'])
        # print(job_exists)
        if not job_exists:
            new_job = JobsModel(title=args['title'],category=args['category'],
                                responsibility=args['responsibility'],
                                company=args['company'],salary=args['salary'],
                                location=args['location'])
            add_book = jobs.append(new_job)
            return  make_response(jsonify({"status": 201, "data": [{'message': 'job succesfully added',
                                                                    'job':new_job.serialize()}]}), 201)
        return abort(make_response(jsonify({'message':'job Already exists'}),400))

api.add_resource(AddJob,'/jobs')