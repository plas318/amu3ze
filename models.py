from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db
from flask_login import UserMixin
# Define many to many association table for "likes"

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    # Define one to many Relationship with playlist model
    created = db.relationship('Playlist', backref="creator")
    
    like_table = db.relationship('LikesTable', back_populates='user', cascade='all, delete')
    def __repr__(self) -> str:
        return f'User : id: {self.id} email: {self.email} pw: {self.password}'
    
class Playlist(db.Model):
    __tablename__ = "playlist"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    date = db.Column(db.DateTime, default=datetime.now)
    
    # Reference to the user whom created the playlist
    user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
    # Reference the Likes model with secondary ref to association table
    
    like_table = db.relationship('LikesTable', back_populates='playlist', cascade='all, delete')
    
    def __repr__(self) -> str:
        return f'Playlist: {self.name} listId: {self.url} created-user: {self.user}'
    


class LikesTable(db.Model):
    __tablename__= "like_table"
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id"), nullable=False)
    # likes_id = db.Column(db.Integer, db.ForeignKey("likes.id"), nullable=False)
    
    __table_args__ = (db.UniqueConstraint(user_id, playlist_id),)
    
    user = db.relationship('User', back_populates='like_table')
    playlist = db.relationship('Playlist', back_populates='like_table')
    # likes = db.relationship('Likes', back_populates='like_table')
    
    def __repr__(self) -> str:
        return f'Likes Table : {self.user} {self.playlist}'