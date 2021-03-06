from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SelectField
from application import db
from application.groups.models import Groups


class TaskForm(FlaskForm):

    name = StringField("Task name", [validators.Length(min=1), validators.Length(max=20)])
    done = BooleanField("Done")
    groups_query = Groups.query.all()
    lista = [(u.id, u.name) for u in groups_query]
    groups = SelectField(u'Group', choices=lista)


    class Meta:
        csrf = False
