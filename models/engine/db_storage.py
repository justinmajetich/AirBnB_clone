#!/usr/bin/python3
""" Database Storage Engine """

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """ Database Storage """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the Database Storage """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                environ['HBNB_MYSQL_USER'],
                environ['HBNB_MYSQL_PWD'],
                environ['HBNB_MYSQL_HOST'],
                environ['HBNB_MYSQL_DB']
            ),
            pool_pre_ping=True
        )
        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Return a dictionary of all objects """
        objs_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objs_dict[key] = obj
        else:
            for cls in Base.__subclasses__():
                for obj in self.__session.query(cls):
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    objs_dict[key] = obj
        return objs_dict

    def new(self, obj):
        """ Add an object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes to the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete an object from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)

