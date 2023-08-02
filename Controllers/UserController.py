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
        try:
            if request.is_json:
                params = request.get_json()
                name = params.get('name', None)
                description = params.get('description', None)

            else:
                raise ValueError('data type error')
                
            self.UserService.createNew(name , description)
            return make_response(
                jsonify(
                    {"success":"true"}
                ), 200)

        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),400)

