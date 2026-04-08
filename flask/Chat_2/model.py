from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone
from email.policy import default
from wsgiref.simple_server import server_version

from sqlalchemy.orm import backref

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    

    def __repr__(self):
        return f'<User {self.username}>'
class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text,nullable=False)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    message_color = db.Column(db.String(20), default="#ffffff")

    user = db.relationship('User',backref=db.backref('messages',lazy=True))







