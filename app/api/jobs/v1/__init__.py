from flask_restplus import Api
from flask import Blueprint
from app.api.jobs.v1.views import api as ns2

jobs_v1 = Blueprint('jobs_v1',__name__)

api = Api(jobs_v1, title='Travailler',
              default_label='Travailler endpoints',
              default='Travailler')

api.add_namespace(ns2, path='/api/v1')