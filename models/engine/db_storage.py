#!/usr/bin/python3
"""This is the file Dbstorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy as db
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.base_model import Base


class DBStorage:
    '''New Engine'''

    __engine = None
    __session = None

    def __init__(self):
        '''Constructor'''
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        database = environ.get('HBNB_MYSQL_DB')
        hbn_env = environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                .format(user, password, host, database),
                pool_pre_ping=True)
        if hbn_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''return a dictionary '''
        class_list = ["State", "City", "User", "Place"]
        dict_to_return = {}
        if cls is None:
            for table in class_list:
                query = self.__session.query(eval(table)).all()
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dict_to_return[key] = obj
        else:
            query = self.__session.query(eval(cls)).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dict_to_return[key] = obj
        return dict_to_return

    def new(self, obj):
        '''add the object to the current database session '''
        if obj:
            self.__session.add(obj)

    def save(self):
        ''' commit all changes of the current database session '''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session '''
        if obj:
            result = self.__session.query(eval(obj)).\
                    filter(id == obj.id).first()
            result.delete()

    def reload(self):
        '''create all tables in the database (feature of SQLAlchemy) '''
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                expire_on_commit=False, autoflush=False)
        self.__scoop = scoped_session(session_factory)
        self.__session = self.__scoop()

    def close(self):
        ''' teehee '''
        self.__session.close()
