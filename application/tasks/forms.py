from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SelectField
from application import db
from application.groups.models import Group


class TaskForm(FlaskForm):

    name = StringField("Task name", [validators.Length(min=1), validators.Length(max=20)])
    done = BooleanField("Done")
    vari = Group.query.all()
    lista = [(u.id, u.name) for u in vari]
    print("hellohihihihhi{}".format(vari))
    print("lista: {}".format(lista))
    myField = SelectField(u'Group', choices=lista)

    class Meta:
        csrf = False
