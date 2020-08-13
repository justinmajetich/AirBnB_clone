#!/usr/bin/python3
"""Defining DBStorage engine """
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """initializing connection with database according
    to environment variables"""
    __engine = None
    __session = None

    def __init__(self):
        """"""
        user = getenv('HBNB_MYSQL_USER')
        paswd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        tmp = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, paswd, host, database),
            pool_pre_ping=True
            )

        if tmp is 'test':
            Base.metadata.drop_all(self.__engine)
            # If fails remember to review this part

    def all(self, cls=None):
        """Lists all objects depending of the class or all types of objects """
        classes = {
            'State': State,
            'City': City,
            'User': User
            }

        dictionary = {}

        if cls is None:
            for key, value in classes.items():
                objetos = self.__session.query(value).all()
                for obj in objetos:
                    dictionary[type(obj).__name__ + "." + obj.id] = obj
        elif cls:
            # comment to review
            objetos = self.__session.query(cls).all()
            for obj in objetos:
                dictionary[type(obj).__name__ + "." + obj.id] = obj

        return(dictionary)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        and create the current database session """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
            )
        self.__session = Session()
