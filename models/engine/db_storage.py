#!/usr/bin/python3
"""
Database Module for HBNB project
"""

import os
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    Database storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get('HBNB_MYSQL_USER'),
            os.environ.get('HBNB_MYSQL_PWD'),
            os.environ.get('HBNB_MYSQL_HOST'),
            os.environ.get('HBNB_MYSQL_DB')))
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.__session = scoped_session(sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.__engine))
        else:
            BaseModel.__table__.drop(self.__engine)
            BaseModel.__table__.create(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects
        """
        objs = []
        if cls is not None:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(Place).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()
        return objs

    def new(self, obj):
        """
        Adds a new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the database
        """
        BaseModel.__table__.drop(self.__engine)
        BaseModel.__table__.create(self.__engine)

    def close(self):
        """
        Closes the current database session
        """
        self.__session.close()
