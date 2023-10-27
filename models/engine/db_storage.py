#!/usr/bin/python3
""" DBStorage Module for HBNB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage

class DBStorage(FileStorage):
    """ DBStorage class """
    __engine = None
    __session = None
    _FileStorage_objects = {}

    def __init__(self):
        """ Set up the connection to the database """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
                    pool_pre_ping=True)
        """ Drop all tables if HBNB_ENV is "test" """
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query objects from database session """
        objects = {}
        if cls is not None:
            query_result = self.__session.query(cls)
        else:
            query_result = self.__session.query(User, State, City, Amenity, Place, Review)

        for obj in query_result:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)

        return objects

    def new(self, obj):
        """ Add object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current database session if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create tables in database and configure as scoped session """

    def close(self):
            """Closing the session"""
            self.__session.close()
