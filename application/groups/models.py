from application import db
from application.models import Base

class Group(Base):


    name = db.Column(db.String(144), nullable=False)
    # tasks = db.relationship("Task", backref='group', lazy=True)
    #task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=True)
    # uutta

    # tasks = db.relationship("Task", backref='group', lazy=True)

    def __init__(self, name):
        self.name = name
