#!/usr/bin/python3
"""
This module defines new engine DBStorage
"""

from os import getenv
import sqlalchemy
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base


class DBStorage:
    """
    Class definition
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        """

        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary with all objects depending on class name"""
        classes = {"City": City, "State": State, "User": User, "Place": Place,
                   "Review": Review, "Amenity": Amenity}
        new_dict = {}
        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        else:
            for clss in classes:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """"add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        and create the current database session"""
        Base.metadata.create_all(self.__engine)
        # call_session is the factory
        call_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(call_session)
        self.__session = Session

    def close(self):
        """
        No seeee
        """
        self.__session.remove()
