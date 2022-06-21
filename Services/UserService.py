from Models.User import User
from flask_sqlalchemy import SQLAlchemy

class UserService:
    def __init__(self):
        self.db = SQLAlchemy()
        
    def createNew(self,name , description):
        if name=="":
            raise ValueError('name required')
        if description=="":
            raise ValueError('description required')
        user = User(name , description)
        self.db.session.add(user)
        self.db.session.commit()
