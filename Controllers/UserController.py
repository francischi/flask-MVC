from flask import request,make_response,jsonify
from Services.UserService import UserService
class UserController:
    def __init__(self):
        self.UserService = UserService()

    def getAll(self):
        try:
            result = self.UserService.getAll()
            return make_response(
                    jsonify(
                        {"success":"true",
                        "result":result}
                    ),200)
        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),400)

    def createUser(self):
        params = request.values
        try:
            if params['name']== "":
                raise ValueError('name required')
            if params['description']== "":
                raise ValueError('description required')
                
            self.UserService.createNew(params)
            return make_response(
                jsonify(
                    {"success":"true"}
                ), 200)

        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),400)

