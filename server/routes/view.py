from imports import *

view = Blueprint('view', __name__)

@view.route('/')
def index():
    return render_template('view/home.html')

@view.route('/login')
def login():
    return render_template('auth/login.html')

@view.route('/signup')
def signup():
    return render_template('auth/signup.html')