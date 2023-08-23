#!/usr/bin/python3
"""Defines a class to manage DBStorage for HBNB project"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ Database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize SQL DBStorage """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns dictionary for models in current session """
        objects = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """ Adds objects to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes DB session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables and create a new session """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

    def close(self):
        """ Closes the session """
        self.__session.remove()
