from flask_restplus import Api
from flask import Blueprint
from app.api.v2.views.users_views import api as ns3
# from app.api.v1.views.users_views import api as ns2

version2 = Blueprint('version2',__name__)

api = Api(version2, title="Travailler",
            default_label="Travailler Endpoints",
            default="Travailler")

api.add_namespace(ns3,path='/api/v2')