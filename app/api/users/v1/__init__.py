from flask_restplus import Api
from flask import Blueprint
from app.api.users.v1.views import api as ns1

v1 = Blueprint('users_v1',__name__)

api = Api(v1, title='Travailler',
              default_label='Travailler endpoints',
              default='Travailler')

api.add_namespace(ns1, path='/api/v1')