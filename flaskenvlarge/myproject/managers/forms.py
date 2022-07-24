from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Manager: ')
    dept_id = IntegerField('Department ID: ')
    submit = SubmitField('Add Manager to Department')
