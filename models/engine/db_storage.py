#!/usr/bin/python3
"""This module defines a class to manage dbstorage for hbnb clone"""
import json
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from models.base_model import Base, BaseModel
import os


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """Returns a dictionary of models currently in storage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True))
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return a dictionary of objects"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if cls is not None:
            query_obj = self.__session.query(cls).all()
        else:
            list_class = [User, State, City, Amenity, Place, Review]
            for x in list_class:
                query_obj += self.__session.query(x).all()
        for v in query_obj:
            id_key = type(v).__name__ + "." + v.id
            new_dict[id_key] = v
        return new_dict

    def new(self, obj):
        """Add the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete the obj from the DB if is not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Method reload"""
        Base.metadata.create_all(self.__engine)
        session_registry = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        self.__session = scoped_session(session_registry)
