#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True,
            )
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the DB"""
        if cls is not None:
            items = self.__session.query(cls).all()
            name = cls.__name__
            return {"{}.{}".format(name, item.id): item for item in items}
        classes = [
            State,
            User,
            Amenity,
            Place,
            City
        ]
        result = {}
        for _class in classes:
            items = self.__session.query(_class).all()
            for item in items:
                result["{}.{}".format(_class.__name__, item.id)] = item
        return result
    
    def new(self, obj):
        """Adds a new object to the current session"""
        self.__session.add(obj)
    
    def save(self):
        """Commits changes to the database"""
        self.__session.commit()
    
    def delete(self, obj):
        """Deletes an object from the current session"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)

        # Creating a thread safe session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)

        self.__session = Session()

    def close(self):
        """Close the current db session"""
        self.__session.close()