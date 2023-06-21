#!/usr/bin/python3
"""Sql database storage module"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
         # Retrieve MySQL configuration from environment variables
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        # Create the engine
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, pwd, host, db),
            pool_pre_ping=True)

        # Drop all tables if HBNB_ENV is 'test'
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Create all tables
        Base.metadata.create_all(self.__engine)

        # Create the session
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Query all objects based on class"""
        objects = {}
        if cls:
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for cls in Base.__subclasses__():
                query = self.__session.query(cls)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and recreate the database session"""
        self.__session = Base.metadata.create_all(self.__engine)
        sesh = (sessionmaker(
            bind=self.__engine,
            expire_on_commit=False))
        Session = scoped_session(sesh)
        self.__session = Session()
