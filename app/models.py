from . import db
from datetime import datetime

class User(db.Model):
    '''
    User tables
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    about = db.Column(db.Text())
    avatar = db.Column(db.String(64))

    created_at = db.Column(db.DateTime, index=True, default=datetime.now)


class Pitch(db.model):
    '''
    Pitches table
    '''
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref="pitches", lazy="dynamic")

    created_at = db.Column(db.DateTime, index=True, default=datetime.now)

class Category(db.Model):
    '''
    Pitch categories table
    '''
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    picture_path = db.Column(db.String(64))
    post = db.relationship('Pitch', backref='category', lazy='dynamic')

    # get all categories
    @staticmethod
    def get_all_categories():
        return Category.query.all()

    # save category
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Category {self.name}'

class Vote(db.Model):
    '''
    Votes table
    '''
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    pitch = db.relationship('Pitch', backref='votes', lazy="dynamic")

class Role(db.Model):
    '''
    Roles table
    '''
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'Role {self.name}'
