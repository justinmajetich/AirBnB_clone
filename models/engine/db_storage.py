#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in SQL format"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates Instance into DBStorage"""
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                      .format(dialect, driver, user, passwd,
                                              host, db), pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current database session"""

        classes = {City, State, User, Place, Amenity, Review}

        dictionary = {}
        if cls in classes:
            dic = self.__session.query(cls).all()
            for el in dic:
                key = el.__class__.__name__ + '.' + el.id
                dictionary[key] = el
        elif cls is None:
            dic = []
            for cls in classes:
                dic += self.__session.query(cls).all()
            for el in dic:
                key = el.__class__.__name__ + '.' + el.id
                dictionary[key] = el

        return dictionary

    def new(self, obj):
        """add new object to DB"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object if exist"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))

    def close(self):
        """call remove method on the private session attribute
        self.__session or close on the class Session"""
        self.__session.remove()
