#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


classes_list = {'User', 'Place', 'State', 'City', 'Amenity', 'Review'}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        # Return the value of the environment variable key as a string if it exists
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost{}/{}'.format(os.getenv("HBNB_MYSQL_USER"), os.getenv("HBNB_MYSQL_PWD"), os.getenv("HBNB_MYSQL_HOST"), os.getenv("HBNB_MYSQL_DB")),
        pool_pre_ping=True)

        # drop all tables if the environment variable HBNB_ENV is equal to test
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        """
        if cls is None:
            My_obj = self.__session.query(State).all()
            My_obj.extend(self.__session.query(City).all())
            My_obj.extend(self.__session.query(User).all())
            My_obj.extend(self.__session.query(Place).all())
            My_obj.extend(self.__session.query(Review).all())
            My_obj.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            My_obj = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in My_obj}

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the db (all classes who inherit from Base are
        imported before calling)
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)

        # scoped_session - to make sure your Session is thread-safe
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ close the session """
        self.__session.close()
