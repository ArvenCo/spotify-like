from imports import *

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    
class Music(db.Model):
    __tablename__ = 'musics'
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=True)
    path = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False, unique=True)
    duration = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    albums = db.relationship('Album', backref='artists', lazy=True)

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    name = db.Column(db.String, nullable=False)
    musics = db.relationship('Music', backref='albums', lazy=True)


    