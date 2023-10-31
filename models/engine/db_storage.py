#!/usr/bin/python3
""" module for DBStorage class """
import os
import sys
from os import getenv
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

classes = {
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review
}

class_list = [
    BaseModel,
    User,
    Place,
    State,
    City,
    Amenity,
    Review
]


class DBStorage:
    """This class manages storage of hbnb models into database"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation of DBStorage engine"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
            )

    def all(self, cls=None):
        """query all objects - specific to cls var, if supplied"""
        obj_dict = {}
        for key in classes.keys():
            if cls == key or cls == classes[key] or cls is None:
                obj_list = self.__session.query(classes[key]).all()
                for obj in obj_list:
                    obj_dict[f'{obj.__class__.__name__}.{obj.id}'] = obj
        return obj_dict

    def new(self, obj):
        """adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from current database session, obj argument supplied"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create tables and database session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
