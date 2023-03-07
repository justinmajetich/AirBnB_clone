#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import sqlalchemy
import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
from os import getenv

classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class DBStorage():
    __engine = None
    __session = None
    __objects = {}

    def __init__(self):
        """Creates engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        
        self.__engine = sqlalchemy.create_engine(
             "mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database),
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        self.user = self.__session.query(User)
        self.state = self.__session.query(State)
        self.city = self.__session.query(City)
        self.amenity = self.__session.query(Amenity)
        self.place = self.__session.query(Place)
        self.review = self.__session.query(Review)

        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            spec_dict = {}
            for key, val in self.__objects.items():
                if cls == type(val):
                    spec_dict[key] = val
            return spec_dict
        return self.__objects

    def new(self, obj):
        """Adds new object to database session"""
        self.__session.add(obj)

    def save(self):
        """Commits changes to database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes current instance from the storage"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """Creates current database session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
