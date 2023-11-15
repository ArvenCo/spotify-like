from imports import *
import server.controller.auth as AuthController
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    return AuthController.login()

@auth.route('/signup', methods=['POST'])
def signup():
    return AuthController.signup()

@auth.route('/logout', methods=['GET'])
def logout():
    return AuthController.logout()