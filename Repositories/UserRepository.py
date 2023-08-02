from OrmModels.User import User as OrmUser
from OrmModels.DB import session

class UserRepository:
    def __init__(self):
        self.db = session
        
    def getAll(self):
        return "="

    def createNew(self,name , description):
        user = OrmUser(name , description)
        self.db.add(user)
        self.db.commit()