from flask import Flask,Blueprint,jsonify
from app.api.users.v1 import users_v1
from app.api.jobs.v1 import jobs_v1
from instance.config import config_by_name

def create_app(config_name='dev'):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(users_v1)
    app.register_blueprint(jobs_v1)

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(error=404, text='could not find requested data'), 404
    
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error=404, text='Invalid input'), 400

    return app