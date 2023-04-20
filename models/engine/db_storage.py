#!/usr/bin/python3

"""Module that sets up DBstorage using SQLAlchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, scoped_session

class DBStorage:
    """DB storage for database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
    """makes an instance"""
    user = os.getenv('HBNB_MYSQL_USER')
    password = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    db = os.getnenv('HBNB_MYSQL_DB')
    self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user, password, host, db), pool_pre_ping=True)
    if os.getenv('HBNB_ENV') == 'test':
        Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
