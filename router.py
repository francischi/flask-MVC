from flask import Blueprint
from Controllers.UserController import UserController
allRoute = Blueprint('allRoute', __name__)

@allRoute.route('/user', methods=['POST'])
def createUser():
    return UserController().createUser()

@allRoute.route('/users', methods=['GET'])
def getAll():
    return UserController().getAll()