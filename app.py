from imports import *
from server.routes import *
from server.models import *

app = Flask(__name__)

app.config.update({
    'SQLALCHEMY_DATABASE_URI' : 'sqlite:///spotify_like.db',
})


app.register_blueprint(view)
db.init_app(app)


def main():
    return app.run(debug=True, host='0.0.0.0', port=1039)

if __name__ == '__main__':
    main()