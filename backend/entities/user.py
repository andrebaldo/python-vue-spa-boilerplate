# file path: /backend/entities/user.py
# Defines the User data model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

class User(SQLAlchemy().Model):
    __tablename__ = 'User' # Name of the table in our database
    # Defining the columns
    userId = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    mobilePhone = Column(String(80), unique=False, nullable=True)