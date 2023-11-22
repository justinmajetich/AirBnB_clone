#!/usr/bin/python3
"""Class that is new for sqlAlchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scopedd_session
from models.base_model import Base
from os import getenv

class DBStorgae:
    """Class created for tables in environment"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DBStorage."""
        self.__engine = created_engine('mysql+mysqldb://{}.{}@{}:3306/{]'
                .format(getenv('HBNB_MYSQL_USER')
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects or the filtered by class"""
        objects = {}
        if cls:
            for obj in self.__session.query(cls).all():
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objects[key] = obj

        else:
            for obj in self.__session.query(State).all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
            for obj in self.__session.query(City).all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        
        return objects

    def new(self, obj):
        """Adss a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reloads the database."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
