from imports import *
from server.models import *

def index():
    mp3s = Music.query.all()
    data= []
    for mp3 in mp3s:
        album_name = None
        artist_name = None
        if mp3.album_id is not None:
            album = Album.query.get(mp3.album_id)
            artist = Artist.query.get(album.artist_id)
            artist_name = artist.name
            album_name = album.name
            
        data.append({
            'title': mp3.title,
            'duration': mp3.duration,
            'path': mp3.path,
            'album': album_name,
            'artist' : artist_name
        })
    return data