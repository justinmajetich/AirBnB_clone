#!/usr/bin/python3
'''This is a module'''
from sqlalchemy import create_engine
import os
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models import *

valid_classes = ['City', 'State', 'User', 'Amenity', 'Place', 'Review']


class DBStorage:
    '''A db storage class'''
    __engine = None
    __session = None

    def __init__(self):
        '''An init function'''
        username = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(username, passwd, host, db),
                                      pool_pre_ping=True)

        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)

        if cls=None, query all types of objects
        (User, State, City, Amenity, Place and Review)

        Return: dictionary
        '''
        storage = {}
        if (cls):
            for instance in self.__session.query(cls):
                storage[instance.id] = instance
        elif (cls is None):
            for cls_name in valid_classes:
                for instance in self.__session.query(eval(cls_name)):
                    storage[instance.id] = instance
        return storage

    def new(self, obj):
        '''
        add the object to the current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
        commit all changes of the current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        delete from the current database session obj if not None
        '''
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        '''
        create all tables in the database
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
