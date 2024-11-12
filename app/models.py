from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import Column, DateTime, func


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(64), db.ForeignKey('user.username'))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


class A_treat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    description = db.Column(db.Text)
    foto = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<A_treat {self.title}>'


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    description = db.Column(db.Text)
    foto = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Pizza {self.title}>'


class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    description = db.Column(db.Text)
    foto = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Drinks {self.title}>'


class Today(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Integer)
    time = db.Column(db.String(50))
    foto = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Today {self.title}>'
