# databaseCreation.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# Make sure that you have a SQL Server runing in your local host, check also the instance
# name, in some instalations the server path will be 'localhost/SQLEXPRESS' in this case, 
# update the SERVER variable below accordingly
# This script creates the tables User and UserSession, just execute:$python databaseCreation.py
# from your command pront, tested just on Windows.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

with open('./config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)

DATABASE_CONNECTION = config['database_connection_string']
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db = SQLAlchemy(app)


import flask_login


class User(db.Model, flask_login.mixins.UserMixin):
    __tablename__ = 'User' # Name of the table in our database
    # Defining the columns
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    mobilePhone = db.Column(db.String(80), unique=False, nullable=True)
    def get_id(self):
        return text_type(self.userId)

class UserSession(db.Model):
    __tablename__ = 'UserSession' # Name of the table in our database
    # Defining the columns
    userSessionId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    loginDate = db.Column(db.DateTime, nullable=False)
    expireDate = db.Column(db.DateTime, nullable=False)
    loggedOut = db.Column(db.Boolean, nullable=False)
    jwToken = db.Column(db.String(4000), nullable=False)
    url = db.Column(db.String(4000), nullable=True)
    logoutDate = db.Column(db.DateTime, nullable=True)



db.create_all()
db.session.commit()