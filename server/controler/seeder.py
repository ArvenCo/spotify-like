import os
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from datetime import timedelta
from server.models import *

def convert_delta(dlt: timedelta) -> str:
    minutes, seconds = divmod(int(dlt.total_seconds()), 60)
    return f"{minutes}:{seconds:02}"

def to_db(dir: str, filename: str):
    data = ID3(dir)
    mp3 = MP3(dir)
    duration = convert_delta(timedelta(seconds=mp3.info.length))
    
    title, artist, album = filename, None, None

    if data.getall('TIT2'):
        title = str(data['TIT2'])
    
    if data.getall('TPE2'):
        artist =str(data['TPE2']) 

    if data.getall('TALB'):
        album = str(data['TALB'])
        
    return {
        'title' : title,
        'artist' : artist,
        'album' : album,
        'duration' : duration,
    }


def save(id3: to_db, path: str):
    music = Music.query.filter_by(title=id3['title']).first()
    if music is None:
        music = Music(title=id3['title'], path=path, duration=id3['duration'])
        db.session.add(music)
        db.session.commit()
        if id3['artist'] is not None:
            artist = Artist.query.filter_by(name=id3['artist']).first()
            album = Album.query.filter_by(name=id3['album']).first()

            if artist is None:
                artist = Artist(name=id3['artist'])
            db.session.add(artist)
            db.session.commit()


            if album is None :
                if id3['album'] is None: album = Album(artist_id=artist.id, name='None')
                else: album = Album(artist_id=artist.id, name=id3['album'])

            db.session.add(album)
            db.session.commit()

            music.album_id = album.id
            db.session.commit()
            
            


def files_in(str_dir: str):
    # directory = os.fsencode(str_dir)
    for f in os.listdir(str_dir):
        filename = os.fsdecode(f)
        if filename.endswith(".mp3"):
            filepath = os.path.join(str_dir, filename)
            id3 = to_db(filepath, filename)
            
            save(id3, filepath)
            # database save
            
        else:
            continue
    



def main():
    files_in('static\mp3')
    pass

if __name__ == "__main__":
    main()