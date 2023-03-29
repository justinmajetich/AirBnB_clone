#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine, inspect, MetaData
from datetime import datetime
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv

classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """Creates engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
             "mysql+mysqldb://{}:{}@{}/{}".format(user,
                                                  password,
                                                  host,
                                                  database),
             pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        cls_lst = ["Review", "City", "State", "User", "Place", "Amenity"]
        obj_lst = []
        if cls is None:
            for cls_type in cls_lst:
                obj_lst.extend(self.__session.query(cls_type).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj_lst = self.__session.query(cls).all()
        return {"{}.{}".format(type(obj).__name__,
                               obj.id): obj for obj in obj_lst}

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
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """Closes a session"""
        if self.__session:
            self.__session.remove()
