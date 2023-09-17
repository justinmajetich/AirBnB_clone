#!/usr/bin/python3
"""This module defines a class to manage database based
file storage for hbnb clone"""
# import json
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from urllib.parse import quote_plus

from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a `DBStorage` object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            environ['HBNB_MYSQL_USER'], quote_plus(environ['HBNB_MYSQL_PWD']),
            environ['HBNB_MYSQL_HOST'], environ['HBNB_MYSQL_DB']),
            pool_pre_ping=True)
        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            objs = []
            for obj_cls in (State, City):
                objs.extend(list(self.__session.query(obj_cls)))
            return {obj.__class__.__name__ + '.' + obj.id: obj for obj in objs}
        return {obj.__class__.__name__ + '.' + obj.id: obj for obj in
                self.__session.query(cls)}

    def new(self, obj):
        """Adds new object to to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def delete(self, obj=None):
        """Deletes `obj` from from the current database session"""
        if not obj:
            return
        self.__session.delete(obj)
