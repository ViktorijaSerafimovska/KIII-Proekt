from app import db
from datetime import datetime

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(50))
    birth_year = db.Column(db.Integer)
    bio = db.Column(db.Text)
    exhibits = db.relationship('Exhibit', backref='artist', lazy=True)

class Exhibit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    location = db.Column(db.String(100))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    ticket_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Visitor {self.name}>'
