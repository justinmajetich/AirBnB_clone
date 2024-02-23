#!/usr/bin/python3

"""This module defines a class for creating the engine DBStorage"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


Base = declarative_base()

class DBStorage:
    """This class manages storage of hbnb models in database format"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine for db_storage"""

        # Set ENV Variables
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        # Set DB connection
        connect = "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db)

        # Create engine
        self.__engine = create_engine(connect, pool_pre_ping=True)

        # Drop tables if in test environment
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create the session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """Implement query and return as dictionary"""
        pass

    def new(self, obj):
        """Add object to session"""
        pass

    def save(self):
        """Commit session changes"""
        pass

    def delete(self, obj=None):
        """Delete object from session"""
        pass

    def reload(self):
        """Recreate tables and create new session"""
        pass