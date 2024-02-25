#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of hbnb models using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of DBStorage"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db = os.getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, db), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)
            
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """Query on the current database session all objects"""
        from models import classes

        objects = {}
        if cls:
            request = self.__session.query(classes[cls])
            for obj in request:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for cls in classes.values():
                request = self.__session.query(cls)
                for obj in request:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects


    def new(self, obj):
        """Adds new object to storage"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
