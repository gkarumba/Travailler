from flask_restplus import Api
from flask import Blueprint
from app.api.v1.views.jobs_views import api as ns1
from app.api.v1.views.users_views import api as ns2

version1 = Blueprint('version1',__name__)

api = Api(version1, title="Travailler",
            default_label="Travailler Endpoints",
            default="Travailler")

api.add_namespace(ns1,path='/api/v1')
api.add_namespace(ns2,path='/api/v1')