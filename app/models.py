from wtforms import form, fields
from flask_admin.contrib.pymongo import ModelView


class DataForm(form.Form):
    mMessage = fields.StringField('mMessage')
    client_id = fields.SelectField('client_id')


class DataView(ModelView):
    column_list = ('_id', 'client_id', 'mMessage')
    form = DataForm
