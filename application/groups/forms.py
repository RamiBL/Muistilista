from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class GroupsForm(FlaskForm):
    name = StringField("Group name", [validators.Length(min=1), validators.Length(max=20)])


    class Meta:
        csrf = False
