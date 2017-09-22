from wtforms import form, fields
from flask_admin.contrib.pymongo import ModelView
from flask_admin.contrib.pymongo.filters import FilterEqual, FilterLike


class DataForm(form.Form):
    mMessage = fields.StringField('mMessage')
    client_id = fields.StringField('client_id')


class DataView(ModelView):
    can_create = False
    can_edit = True
    column_filters = (
        FilterEqual(column='client_id', name='client id'),
        FilterLike(column='client_id', name='client id'))
    column_list = ('client_id', 'mMessage')
    form = DataForm
