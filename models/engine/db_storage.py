#!/usr/bin/python3
"""This module defines a class to manage SQL storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.__init__ import storage
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Init engine"""
        data = [0, 0, 0, 0]
        data[0] = os.getenv("HBNB_MYSQL_USER")
        data[1] = os.getenv("HBNB_MYSQL_PWD")
        data[2] = os.getenv("HBNB_MYSQL_HOST") or "localhost"
        data[3] = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{0}:{1}@{2}/{3}"
            .format(data[0], data[1], data[2], data[3]),
            pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects in the database"""
        new_dict = {}
        if cls is not None:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            objects.extend(self.__session.query(State).all())
            objects.extend(self.__session.query(City).all())
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_temp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_temp)
        self.__session = Session()
    
    def close(self):
        """Close the session"""
        self.__session.close()