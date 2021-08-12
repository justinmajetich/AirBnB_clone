#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """Database Storage Engine Class """
    __engine = None
    __session = None

    def __init__(self):
        """ init function """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)

        if (HBNB_ENV == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on current db session (self.__session) all obj depending
        on class name (arg cls) """
        all_objs = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    all_objs[key] = obj
        return (all_objs)

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """
        reload method
        creates all tables in the database
        creates the current database session (self.__session)
        from the engine (self.__engine) by using a sessionmaker -
        """
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, \
                                   expire_on_commit=False)
        Session = scoped_session(new_session)
        self.__session = Session()

    def close(self):
        """ close session """
        if self.__session:
            self.__session.close()
