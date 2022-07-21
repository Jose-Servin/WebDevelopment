from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Department: ')
    submit = SubmitField('Add Department')


class DelForm(FlaskForm):
    id = IntegerField("ID of Department to remove: ")
    submit = SubmitField('Delete Department')
