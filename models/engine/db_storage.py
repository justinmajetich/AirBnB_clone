#!/usr/bin/env python3
''' Module for database storage class.
'''
from datetime import datetime
from sqlalchemy.orm import (
        declarative_base, relationship, sessionmaker, scoped_session)
from sqlalchemy import (
        create_engine, Column, ForeignKey, Integer, String, Numeric, Date)
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place, place_amenity
from models.review import Review
import os


class DBStorage:
    ''' Class definition for database storage class.
    '''
    __engine = None
    __session = None

    def __init__(self):
        # Create the engine
        dialect = 'mysql'
        driver = 'mysqldb'
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        connect_string = f'{dialect}+{driver}://{user}:{pwd}@{host}/{db}'
        self.__engine = create_engine(connect_string, pool_pre_ping=True)

        # Drop all tables if test environment
        env = os.getenv('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        ''' Returns all objects, or only those of class, cls, if not None.
            Args:
                cls (type): a class whose objects to return
            Return:
                dict: same as is returned by
                FileStorage.all() - a dictionary of id-object pairs.
        '''
        # Get the stored scoped session
        sess = self.__session()

        # Get list of objects
        if cls:
            # Get a cls objects only
            objs = sess.query(cls).all()
        else:
            # Get all objects
            classes = [User, State, City, Amenity, Place, Review]
            objs = []
            for cls in classes:
                cls_objs = sess.query(cls).all()
                objs.extend(cls_objs)

        # Compose a dictionary of the objects
        dct = {}
        for obj in objs:
            key = obj.__class__.__name__ + '.' + obj.id
            dct.update({key: obj})

        return dct

    def new(self, obj):
        ''' Adds obj to the current database session.
        Args:
            obj (cls): an instance of any of the project's main classes.
        '''
        sess = self.__session()
        sess.add(obj)

    def save(self):
        ''' Commits all changes of the current database session.
        '''
        sess = self.__session()
        sess.commit()

    def delete(self, obj=None):
        ''' Delete obj, if not None, from the current database session.
        '''
        if obj:
            sess = self.__session()
            sess.expunge(obj)  # remove from new list

    def reload(self):
        ''' Creates all tables and the current database session.
        Description: creates all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be
        imported before calling Base.metadata.create_all()
        Also creates the current database session (self.__session) from
        the engine (self.__engine) by using a sessionmaker - the
        option, expire_on_commit, must be set to False;
        and scoped_session - to make sure your Session is thread-safe.
        '''
        # Create a scoped session for thread-safety
        sess_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False
                )  # create session factory
        Session = scoped_session(sess_factory)  # get the scoped sess registry
        self.__session = Session
        ''' Now, a call to self.__session(), i.e. Session(), will
        create a new Session object through sessionmaker, or return the
        existing Session object if one had been earlier created.
        To remove the Session object,
        and thus automatically close it, call Session.remove().
        '''

        # Create all tables
        Base.metadata.create_all(self.__engine)
