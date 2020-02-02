# entities\user.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# Defines the User data model
from flask_sqlalchemy import SQLAlchemy
import flask_login

db = SQLAlchemy()
class User(db.Model, flask_login.mixins.UserMixin):
    __tablename__ = 'User' # Name of the table in our database
    # Defining the columns
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    mobilePhone = db.Column(db.String(80), unique=False, nullable=True)
    def get_id(self):
        return chr(self.userId)
