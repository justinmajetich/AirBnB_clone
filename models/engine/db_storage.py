#!/usr/bin/python3
""" This module defines a class to manage DB storage for hbnb clone """

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage():
    """ Class to manage storage of hbnb models in MySQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ Create DBStorage instance """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True
        ))

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the database based on the class name"""
        obj_dict = {}

        if cls:
            query = self.__session.query(cls)
        else:
            query = self.__session.query(State, City)

        for obj in query:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Adds a new object to the database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and initializes a new session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Closes the current session"""
        self.__session.remove()