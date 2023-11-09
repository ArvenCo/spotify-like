from imports import *

view = Blueprint('view', __name__)

@view.route('/')
def index():
    return "index"

