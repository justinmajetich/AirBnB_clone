#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb"""
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.session import Session

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """DataBase Storage, contains engine and session"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the DBStorage class"""

        mySQL_u = getenv("HBNB_MYSQL_USER")
        mySQL_p = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")

        url = {'drivername': 'mysql+mysqldb', 'host': db_host,
               'username': mySQL_u, 'password': mySQL_p, 'database': db_name}

        self.__engine = create_engine(URL(**url), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        """Adds the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables of the database"""
        Base.metadata.create_all(self.__engine)

        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()

    def close(self):
        """Handles close of DBStorage"""
        self.__session.close()
