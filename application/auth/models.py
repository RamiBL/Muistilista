from application import db, bcrypt
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    tasks = db.relationship("Task", backref='account', lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.username = name
        #self.password = password
        self.password = bcrypt.generate_password_hash(password, 15).decode('utf-8')

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    def is_correct_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def find_users():
        stmt = text("SELECT username FROM Account")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0]})
        return response
    # @staticmethod
    # def find_users_with_no_tasks(:
    #     stmt = text("SELECT Account.id, Account.name FROM Account"
    #                  " LEFT JOIN Task ON Task.account_id = Account.id"
    #                  " WHERE (Task.done IS null OR Task.done = True)"
    #                  " GROUP BY Account.id"
    #                  " HAVING COUNT(Task.id) = 0")
    #     res = db.engine.execute(stmt)
    #     response = []
    #     for row in res:
    #         response.append({"id":row[0], "name":row[1]})
    #     return response
