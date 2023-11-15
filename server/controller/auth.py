from imports import *
from server.models import User,db

login_manager = LoginManager()
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

bcrypt = Bcrypt()

def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('view.index'))
    
    return redirect(url_for('view.login'))

def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    user = User.query.filter_by(username=username).first()
    if user is None and password == confirm_password:
        user = User(username=username, password=bcrypt.generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for('view.index'))

    return redirect(url_for('view.signup'))

def logout():
    logout_user()
    return redirect(url_for('view.login'))