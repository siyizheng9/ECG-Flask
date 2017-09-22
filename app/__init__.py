import os
from flask import Flask, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
import flask_admin as admin
from flask_pymongo import PyMongo
from .models import DataView
from .myadminview import downloadForm
from flask_admin.contrib.fileadmin import FileAdmin
from .data_download import download_data

bootstrap = Bootstrap()
moment = Moment()
myadmin = admin.Admin(name='ECG database', template_mode='bootstrap3')
mongo = PyMongo()


# Create custom admin view
class MyAdminView(admin.BaseView):
    @admin.expose('/', methods=['GET', 'POST'])
    def index(self):
        form = downloadForm()
        if request.method == 'POST':
            collection_name = form.collection.data
            print(request.method, collection_name)
            # data = download_data(mongo.db, collection_name)
            download_data(mongo.db, collection_name)
            filename = collection_name + '.csv'
            return redirect(url_for('mydownloadview.download', path=filename))
        else:
            collections = mongo.db.collection_names()
            choices = [(c, c) for c in collections]
            form.collection.choices = choices
            return self.render('myadmin.html', form=form)


class MyDownloadView(FileAdmin):
    can_upload = False
    can_delete = True
    can_delete_dirs = True
    can_mkdir = True
    can_rename = True


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)

    myadmin.init_app(app)
    mongo.init_app(app)

    path = os.path.join(os.path.dirname(__file__), 'data')
    print('path:', path)

    with app.app_context():
        myadmin.add_view(DataView(mongo.db['kafkatopic']))
        myadmin.add_view(MyAdminView(name="Download"))
        myadmin.add_view(MyDownloadView(path, name='Data file'))

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
