# entities\userSession.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# Defines the UserSession (login session) data model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean

class UserSession(SQLAlchemy().Model):
    __tablename__ = 'UserSession' # Name of the table in our database
    # Defining the columns
    userSessionId = Column(Integer, primary_key=True)
    userId = Column(Integer, nullable=False)
    loginDate = Column(DateTime, nullable=False)
    expireDate = Column(DateTime, nullable=False)
    loggedOut = Column(Boolean, nullable=False)
    jwToken = Column(String(4000), nullable=False)
    url = Column(String(4000), nullable=False)
    logoutDate = Column(DateTime, nullable=False)