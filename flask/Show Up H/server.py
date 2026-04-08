from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone
from email.policy import default
from wsgiref.simple_server import server_version

db = SQLAlchemy()

class computer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ram = db.Column(db.Integer)
    processor = db.Column(db.String(50), nullable=False)
    video_card = db.Column(db.String(50), nullable=False)
    ssd = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(200))

    def __repr__(self):
        return f'Computer {self.name}'


class order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=True)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), server_default=db.func.now(),nullable=False)

    def __repr__(self):
        return f'<Order {self.id} by {self.customer_name}>'