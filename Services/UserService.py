from Models.User import User
from flask_sqlalchemy import SQLAlchemy

class UserService:
    def __init__(self):
        self.db = SQLAlchemy()
        print('UserService init')
    def createNew(self,name , description):
        user = User(name , description)
        self.db.session.add(user)
        self.db.session.commit()
