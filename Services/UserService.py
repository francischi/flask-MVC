from Repositories.UserRepository import UserRepository

class UserService:
    def __init__(self):
        self.UserRepository = UserRepository()
        
    def getAll(self):
        return self.UserRepository.getAll()

    def createNew(self, name :str, description:str):
        if name== "":
            raise ValueError('name required')
        if description== "":
            raise ValueError('description required')
        self.UserRepository.createNew(name,description)
