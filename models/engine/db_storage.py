#!/usr/bin/python3
'''This module defines a class to manage DBStorage'''
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    '''DBStorage class'''
    __engine = None
    __session = None

    def __init__(self):
        '''Initialize DBStorage'''
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
                f"mysql+mysqldb://{user}:{passwd}@{host}/{db_name}",
                pool_pre_ping=True,
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query all objects from db'''
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            classes = [User, Place, State, City, Amenity, Review]
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj

        return objects

    def new(self, obj):
        '''add the object to the current database session'''
        if obj:
            self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database'''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(Session)
