#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """Stablishing connection with a sql database
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate an Object of DBStorage"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,HBNB_MYSQL_HOST,
                                  HBNB_MYSQL_DB, pool_pre_ping=True))

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        if cls=None, query all types of objects
        (User, State, City, Amenity, Place and Review)
        """
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(Amenity).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(User).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
        objects = self.__session.query(cls).all()
        return {object.__clase__.__name__ + '.' + object.id: object for object in objects}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
        self.__session.close()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
        self.__session.close()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.close()

    def reload(self):
        """Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session_secure = scoped_session(session_factory)
        self.__session = session_secure
        self.__session.close()

    def close(self):
        """Closes the session
        """
        self.__session.close()
