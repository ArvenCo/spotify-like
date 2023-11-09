from imports import *
from server.routes import *

app = Flask(__name__)

app.register_blueprint(view)


def main():
    return app.run(debug=True, host='0.0.0.0', port=1039)

if __name__ == '__main__':
    main()