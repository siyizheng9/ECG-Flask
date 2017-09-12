from wtforms import form, fields
from flask_admin.contrib.pymongo import ModelView


class DataForm(form.Form):
    mMessage = fields.StringField('mMessage')


class DataView(ModelView):
    column_list = ('_id', 'mMessage')
    form = DataForm
