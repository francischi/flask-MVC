from flask import Blueprint
from Controllers.UserController import UserController
allRoute = Blueprint('allRoute', __name__)

@allRoute.route('/user/create', methods=['POST'])
def createUser():
    return UserController().createUser()

@allRoute.route('/user/getAll', methods=['GET'])
def getAll():
    return UserController().getAll()