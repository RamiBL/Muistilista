from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TaskForm(FlaskForm):
    name = StringField("Task name", [validators.Length(min=1), validators.Length(max=20)])
    done = BooleanField("Done")

    class Meta:
        csrf = False
