#!/usr/bin/python3
""" Database Storage Module for HBNB project """

import os
import models
import sqlalchemy
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

classNames = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the object"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of all the objects in the database"""
        if not self.__session:
            self.reload()
        objects = {}
        if type(cls) == str:
            cls = classNames.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in classNames.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def reload(self):
        """reloads objects from the database and creates session"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """creates a new object in the database"""
        self.__session.add(obj)

    def save(self):
        """saves the current session to the database"""
        self.__session.commit()

    def get(self, cls, id):
        """Retrieve an object"""
        if cls is not None and type(cls) is str and id is not None and\
           type(id) is str and cls in classNames:
            cls = classNames[cls]
            result = self.__session.query(cls).filter(cls.id == id).first()
            return result
        else:
            return None

    def count(self, cls=None):
        """Count number of objects in storage matching given class name"""
        total = 0
        if type(cls) == str and cls in classNames:
            cls = classNames[cls]
            total = self.__session.query(cls).count()
        elif cls is None:
            for cls in classNames.values():
                total += self.__session.query(cls).count()
        return total

    def delete(self, obj=None):
        """deletes an object from the database"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)
    
    def close(self):
        """Dispose of current session if active and close"""
        self.__session.remove()
