#!/usr/bin/python3
"""
This module defines a class to manage SQL storage for the HBNB clone.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages SQL storage for the HBNB clone"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the engine"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST') or 'localhost'
        db_name = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            "mysql+mysqldb://{0}:{1}@{2}/{3}"
            .format(user, password, host, db_name),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects based on the class name (cls).
        """
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            classes = [State, City]
            for c in classes:
                objs += self.__session.query(c).all()

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        Adds the object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads all tables in the database.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()