from flask import request,make_response,jsonify
from Services.UserService import UserService
class UserController:
    def __init__(self):
        self.UserService = UserService()

    def createUser(self):
        name = request.values.get('name')
        description = request.values.get('description')
        try:
            self.UserService.createNew(name , description)
            return make_response(
                jsonify(
                    {"success":"true"}
                ), 
            200)
        except Exception as msg:
            return make_response(
                jsonify(
                    {"success":"false","message":str(msg)}
                ),
             400)
