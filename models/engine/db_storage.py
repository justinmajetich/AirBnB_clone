#!/usr/bin/python3
"""This module defines the DBStorage class for database storage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage instance"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query objects from the database based on class name"""
        classes = {
            'Amenity': Amenity,
            'City': City,
            'Place': Place,
            'State': State,
            'Review': Review,
            'User': User
        }
        objects = {}

        if cls:
            query = self.__session.query(classes[cls]).all()
            for obj in query:
                key = f'{obj.__class__.__name__}.{obj.id}'
                objects[key] = obj
        else:
            for cls in classes.values():
                query = self.__session.query(cls).all()
                for obj in query:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    objects[key] = obj

        return objects

    def new(self, obj):
        """Add object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()
