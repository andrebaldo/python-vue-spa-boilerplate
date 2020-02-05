# entities\databaseSessionManager.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# This class will return a database SQLAlchemy session,
# classes which want to manipulate data can use it to manipulate the database.
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

with open('./config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)

DATABASE_CONNECTION = config['database_connection_string']
engine = create_engine(DATABASE_CONNECTION, echo=True)

# create a Session
Session = sessionmaker(bind=engine)

class SessionManager(object):
    def __init__(self):
        self.session = Session()