from flask_restplus import Api
from flask import Blueprint
from app.api.users.v1.views import api as ns1

users_v1 = Blueprint('users_v1',__name__)

api = Api(users_v1, title='Travailler',
              default_label='Travailler endpoints',
              default='Travailler')

api.add_namespace(ns1, path='/api/v1')
