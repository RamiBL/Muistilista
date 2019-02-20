from application import db
from application.models import Base

class Group(Base):

    __tablename__ = "group"

    name = db.Column(db.String(144), nullable=False)
    #task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=True)

    tasks = db.relationship("Task", backref='group', lazy=True)
    # tasks = db.relationship("Task", backref='group', lazy=True)

    def __init__(self, name):
        self.name = name
