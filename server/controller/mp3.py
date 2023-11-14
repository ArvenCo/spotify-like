from imports import *
from server.models import *

def index():
    mp3 = Music.query.join(Album.query.join(Artist)).all()

    return mp3