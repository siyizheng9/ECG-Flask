from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class downloadForm(FlaskForm):
    collection = SelectField(u'Collections', coerce=str, choices=[('example', 'example')])
    submit = SubmitField('Download')
