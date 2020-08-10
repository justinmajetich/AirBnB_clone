#!/usr/bin/python3
"""This module defines a Database class to manage file storage"""

from sqlalchemy import create_engine
from base_model import Base
import os


class DBStorage():
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """ """
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')\
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}\
'.format(user, pswd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ """
        instances = {}
        if cls:
            records = self.__session.query(cls).all()
            for row in records:
                key = cls.__name__ + '.' + row.id
                instances[key] = row
        else:
            records = self.__session.query(User, State, City, Amenity, Place, Review)
