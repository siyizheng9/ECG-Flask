from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class downloadForm(FlaskForm):
    client_id = SelectField(u'Client ID', coerce=str, choices=[])
    submit = SubmitField('Download')
