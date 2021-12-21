#!/usr/bin/python3
"""Allows manage storage of hbnb models using SQL Alchemy"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base


class DBStorage():
    """Allows manage storage of hbnb models using SQL Alchemy"""
    __engine = None
    __session = None
    def __init__(self):
        """Create the engine (self.__engine)"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session
        all objects depending of the class name"""
        pass
    
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        and create the current database session by by using a sessionmaker """
        pass
