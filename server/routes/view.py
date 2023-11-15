from imports import *
from server.controller.seeder import main

import server.controller.mp3 as MP3Controller

view = Blueprint('view', __name__)

@view.route('/')
@login_required
def index():
    return render_template('view/home.html', data=MP3Controller.index())

@view.route('/login')
def login():
    return render_template('auth/login.html')

@view.route('/signup')
def signup():
    return render_template('auth/signup.html')

@view.route('/seed')
def seed():
    main()
    return 'done'


    