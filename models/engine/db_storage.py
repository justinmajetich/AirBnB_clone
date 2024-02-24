#!/usr/bin/python3

"""This module defines a class for creating the engine DBStorage"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


Base = declarative_base()

class DBStorage:
    """This class manages storage of hbnb models in database format"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize engine for db_storage"""

        # Set ENV Variables
        user = os.getenv('HBNB_MYSQL_USER', 'hbnb_dev')
        pwd = os.getenv('HBNB_MYSQL_PWD', 'hbnb_dev_db')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')
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
        Session = scoped_session(session_factory)
        self.__session = Session()
        

    def all(self, cls=None):
        """Implement query and return as dictionary"""
        if cls is None:
            result = {}
            for model in [User, State, City, Amenity, Place, Review]:
                for instance in self.__session.query(model).all():
                    key = '{}.{}'.format(model.__name__, instance.id)
                    result[key] = instance
            return result
        else:
            return {f"{cls.__name__}.{instance.id}": instance for instance in self.__session.query(cls).all()}

    def new(self, obj):
        """Add object to session"""
        self.__session.add(obj)

    def save(self):
        """Commit session changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Recreate tables and create new session"""
        Base.metadata.create_all(self.__engine)
        self.__session.close()
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
