from flask import request
from Services.ModelService import ModelService

class ModelController:
    def __init__(self):
        print('before UserService init')
        self.ModelService = ModelService()
        print('after UserService init')

    def createModel(self):
        name = request.values.get('name')
        second = request.values.get('second')
        self.ModelService.createNew(name , "training",second)
        return 'OK'