#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Constructor of DBStorage class"""
        # Create engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        # Drop table if env is test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
  
    def all(self, cls=None):
        """Query on the current database session""" 
        classes = [State, City, User, Place, Review, Amenity]
        if cls is None:
            objs = []
            for c in classes:
                objs += self.__session.query(c).all()
        else:
            objs = self.__session.query(cls).all()
        return {'{}.{}'.format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the engine and initialize a session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
