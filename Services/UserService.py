from OrmModels.User import User as OrmUser
from flask_sqlalchemy import SQLAlchemy
from Models.User import User as ModelUser

class UserService:
    def __init__(self):
        self.db = SQLAlchemy()
        self.ModelUser = ModelUser()
        
    def getAll(self):
        return self.ModelUser.getAll()

    def createNew(self,params):
        user = OrmUser(params['name'] , params['description'])
        self.db.session.add(user)
        self.db.session.commit()
