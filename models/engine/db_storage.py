#!/usr/bin/python3
""" This is the DB Storage class for AirBnB Clone """

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

USER = getenv('HBNB_MYSQL_USER')
PWD = getenv('HBNB_MYSQL_PWD')
HOST = getenv('HBNB_MYSQL_HOST')
DB = getenv('HBNB_MYSQL_DB')

classes = {"City": City, "State": State, "User": User,
        "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage:
    """ Class for DB Engine AirBnB clone """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the constructor """
        db_uri = f'mysql+mysqldb://{USER}:{PWD}@{HOST}:3306/{DB}'
        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session
        Return: a dictionary"""
        dictionary = {}
        if cls:
            query = self.__session.query(eval(cls))
            for obj in query:
                key = f'{type(obj).__name__}.{obj.id}'
                dictionary[key] = obj
        else:
            for _cls in classes.values():
                query = self.__session.query(_cls).all()
                for obj in query:
                    key = f'{type(obj).__name__}.{obj.id}'
                    dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """ Add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close the current SQLAlchemy session """
        self.__session.close()
