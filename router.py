from flask import Blueprint
from Controllers.UserController import UserController
from Controllers.ModelController import ModelController
allRoute = Blueprint('allRoute', __name__)

allRoute.route('/', methods=['POST'])(UserController().createUser)
allRoute.route('/train', methods=['POST'])(ModelController().createModel)