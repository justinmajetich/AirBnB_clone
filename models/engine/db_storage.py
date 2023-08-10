#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from models.state import State
from models.user import User
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages an engine"""
    __engine = None
    __session = None

    def __init__(self):
        """for da DBStorage"""
        ho = getenv("HBNB_MYSQL_HOST")
        envr = getenv("HBNB_ENV")
        ps = getenv("HBNB_MYSQL_PWD")
        us = getenv("HBNB_MYSQL_USER")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f"mysql+mysqldb://{us}:{ps}@{ho}/{db}",
                                      pool_pre_ping=True))

        def all(self, cls=None):
            """ssession database"""
            dicty = {}
            if cls is not None:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    dicty[key] = obj
            return dicty

        def new(self, obj):
            self.__session.add(obj)

        def save(self):
            self.__session.commit()

        def delete(self, obj=None):
            if obj is not None:
                self.__session.delete(obj)

        def reload(self):
            """Loads storage dictionary from a database"""
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
