# file path: /backend/services/database.py
# SQLAlchemy setup and initialization
from flask_sqlalchemy import SQLAlchemy

class Database():
    def getConnectionString(self):
        SERVER = 'localhost'
        DATABASE = 'project001-Alchemy'
        DRIVER = 'SQL Server Native Client 11.0'
        DATABASE_CONNECTION = f'mssql://{SERVER}/{DATABASE}?trusted_connection=yes&driver={DRIVER}'
        return DATABASE_CONNECTION
    def createDatabaseInstance(self, app):
        return SQLAlchemy(app)