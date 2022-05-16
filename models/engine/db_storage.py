#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
import os

class DBStorage:
    ''' This class manages all database storage for HBnB '''
    __engine = None
    __session = None

    def __init__(self):
        ''' Init method for dbstorage'''
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                       user, pwd, host, db), pool_pre_ping=True)
        metadata = MetaData()
        if os.getenv('HBNB_ENV') == 'test':
            metadata.drop_all()

    def all(self, cls=None):
        ''' Returns all cls in DB, or all objects in DB, as a dict'''
        self.__session = Session(self.__engine)
        ret_dict = dict()
        if cls:
            for obj in self.__session.query(cls).all():
                ret_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
        
            class_list = [State, City, User, Place, Review]
            for query_cls in class_list:
                for obj in self.__session.query(query_cls).all():
                    ret_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return ret_dict

    def new(self, obj):
        ''' Add obj to session '''
        self.__session.add(obj)

    def save(self):
        ''' Commit new previous additions '''
        self.__session.commit()

    def delete(self, obj=None):
        ''' Deletes obj if exists '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' Creates all tables from DB '''
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
