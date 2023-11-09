from imports import *

app = Flask(__name__)

def main():
    return app.run(debug=True, host='0.0.0.0', port=1039)

if __name__ == '__main__':
    main()