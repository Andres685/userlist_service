# models.py
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) 
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_title = db.Column(db.String(100), nullable=False)  # Aquí el título, no ID
    watched = db.Column(db.Boolean, default=False)

    user = db.relationship('User', backref='userlist', lazy=True)

    def __repr__(self):
        estado = "Visto" if self.watched else "No visto"
        return f'<UserList user_id={self.user_id} movie_title="{self.movie_title}" - {estado}>'
