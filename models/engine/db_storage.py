#!/usr/bin/python3
"""
    This module defines the engine for the MySQL database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """ database storage """

    __engine = None
    __session = None

    def __init__(self):
        """
        constructor for DBStorage
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query all types of objects
        """
        dict_objects = {}
        if cls is not None:
            for query_obj in self.__session.query(cls).all():
                key = "{}.{}".format(
                    query_obj.__class__.__name__, query_obj.id)
                dict_objects[key] = query_obj
        else:
            all_classes = [State,
                           City, User]

            for clss in all_classes:
                for query_obj in self.__session.query(clss).all():
                    key = "{}.{}".format(
                        query_obj.__class__.__name__, query_obj.id)
                    dict_objects[key] = query_obj
        return dict_objects

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False,)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close session"""
        self.__session.close()
