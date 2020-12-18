#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }


class DBStorage():
    """Database Storage Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates the DBStorage class"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            self.__engine.drop_all()

    def all(self, cls=None):
        """Gets all of cls type or all types if cls is None"""
        newDict = {}
        for _ in classes:
            if cls is None or cls == _:
                objs = self.__session.query(classes[_]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    newDict.update({key: obj})
        return newDict

    def new(self, obj):
        """Adds new object"""
        self.__session.add(obj)

    def save(self):
        """Saves changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj"""
        if obj is not None:
            del obj
            self.save()

    def reload(self):
        """Reloads session with database"""
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()
