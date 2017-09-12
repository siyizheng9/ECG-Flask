from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
from flask_admin import Admin
from flask_pymongo import PyMongo
from .models import DataView

bootstrap = Bootstrap()
moment = Moment()
admin = Admin(name='ECG database', template_mode='bootstrap3')
mongo = PyMongo()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)

    admin.init_app(app)
    mongo.init_app(app)

    with app.app_context():
        admin.add_view(DataView(mongo.db['kafkatopic']))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
