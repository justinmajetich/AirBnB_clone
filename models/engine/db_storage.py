#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ


class DBStorage():
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        Connect to the database through self.__engine.
        Drop all tables if the environment
        variable HBNB_ENV is equal to test.
        """
        self.__engine = create_engine(
            f"mysql+mysqldb://{environ['HBNB_MYSQL_USER']}:{environ['HBNB_MYSQL_PWD']}@{environ['HBNB_MYSQL_HOST']}/{environ['HBNB_MYSQL_DB']}",
            pool_pre_ping=True,
        )
        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            meta = MetaData()
            meta.reflect(bind=self.__engine)
            for table in reversed(meta.sorted_tables):
                self.__engine.execute(table.delete())

    def all(self, cls=None):
        """Returns the list of objects of one type of class. Return a
        dictionary like FileStorage"""
        obj_types = {'User': User, 'State': State, 'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}
        result = {}
        if cls is None:
            for cls_type in obj_types:
                objects = self.__session.query(obj_types[cls_type]).all()
                for obj in objects:
                    key = f"{cls_type}.{obj.id}"
                    result[key] = obj
        else:
            if isinstance(cls, str):
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = f"{cls.__name__}.{obj.id}"
                    result[key] = obj
        return result

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary change to file"""
        self.__session.commit()

    def close(self):
        """Close the session"""
        self.__session.close()

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside,
        if obj is equal to None, do nothing"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create current database session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
