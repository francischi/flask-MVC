from flask import request
from Services.UserService import UserService
class UserController:
    def __init__(self):
        print('before UserService init')
        self.UserService = UserService()
        print('after UserService init')

    def createUser(self):
        name = request.values.get('name')
        description = request.values.get('description')
        self.UserService.createNew(name , description)
        return 'OK'
