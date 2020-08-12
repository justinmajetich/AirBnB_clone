#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in a db"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializate the class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        # Drop all tables stored in this metadata
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dic_obj = {}
        classes = {'State': State, 'City': City, 'User': User,
                   'Place': Place, 'Review': Review, "Amenity": Amenity}
        if cls is None:
            for k, v in classes.items():
                query = self.__session.query(v).all()
                for obj in query:
                    delattr(obj, "_sa_instance_state")
                    dic_obj[obj.__class__.__name__ + "." + str(obj.id)] = obj
        else:
            query = self.__session.query(cls).all()
            for obj in query:
                delattr(obj, "_sa_instance_state")
                dic_obj[obj.__class__.__name__ + "." + str(obj.id)] = obj
        return dic_obj

    def new(self, obj):
        """Add the object to the current database """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database"""
        self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""

        # create all tables in the database
        Base.metadata.create_all(self.__engine)
        # create the current database session
        # expire_on_commit=True, all instances will be fully
        # expired after each commit()
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
