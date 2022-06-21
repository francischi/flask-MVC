from flask import Blueprint
from Controllers.UserController import UserController
allRoute = Blueprint('allRoute', __name__)

allRoute.route('/user/create', methods=['POST'])(UserController().createUser)