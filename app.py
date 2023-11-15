from imports import *
from server.routes import *
from server.models import *
import server.controller.auth as AuthController
app = Flask(__name__)

app.config.update({
    'SQLALCHEMY_DATABASE_URI' : 'sqlite:///spotify_like.db',
    'SECRET_KEY' : 'sasdwq'
})


app.register_blueprint(view)
app.register_blueprint(auth)

db.init_app(app)
AuthController.login_manager.init_app(app)
AuthController.bcrypt.init_app(app)

def main():
    with app.app_context():
        db.create_all()
    return app.run(debug=True, host='0.0.0.0', port=1039)

if __name__ == '__main__':
    main()