# entities\databaseSessionManager.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# This class will return a database SQLAlchemy session,
# classes which want to manipulate data can use it to manipulate the database.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SERVER = 'localhost'
DATABASE = 'project001'
DRIVER = 'SQL Server Native Client 11.0'
DATABASE_CONNECTION = f'mssql://{SERVER}/{DATABASE}?trusted_connection=yes&driver={DRIVER}'
engine = create_engine(DATABASE_CONNECTION, echo=True)

# create a Session
Session = sessionmaker(bind=engine)

class SessionManager(object):
    def __init__(self):
        self.session = Session()