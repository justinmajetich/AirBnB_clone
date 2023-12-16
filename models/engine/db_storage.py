#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = (
            create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                          .format(getenv('HBNB_MYSQL_USER'),
                                  getenv('HBNB_MYSQL_PWD'),
                                  getenv('HBNB_MYSQL_HOST'),
                                  getenv('HBNB_MYSQL_DB')
                                  ), pool_pre_ping=True)
                            )
        
        # drop all tables if the environment variable HBNB_ENV is equal to test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current db all objects depending of the class name """
        if cls:
            return self.__session.query(cls).all()
        else:
            # I AM NOT SURE I UNDERSTAND THE REQUIREMENT HERE
            self.__session.query(BaseModel).all()

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)