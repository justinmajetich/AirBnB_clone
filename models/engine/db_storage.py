#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import importlib
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class is for DBStorage"""
    __engine = None
    __session = None
    __module_names = {
        "BaseModel": "base_model",
        "User": "user",
        "State": "state",
        "City": "city",
        "Amenity": "amenity",
        "Place": "place",
        "Review": "review"
    }

    user = getenv('HBNB_MYSQL_USER')
    pwd = getenv('HBNB_MYSQL_PWD')
    host = getenv('HBNB_MYSQL_HOST')
    db = getenv('HBNB_MYSQL_DB')

    if getenv('HBNB_MYSQL_USER') is None:
        user = "hbnb_dev"
    if getenv('HBNB_MYSQL_PWD') is None:
        pwd = "hbnb_dev_pwd"
    if getenv('HBNB_MYSQL_HOST') is None:
        host = "localhost"
    if getenv('HBNB_MYSQL_DB') is None:
        db = "hbnb_dev_db"

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                self.user, self.pwd, self.host, self.db),
            pool_pre_ping=True
        )

        if self.db == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of everything"""
        output = {}
        if self.__session is not None:
            if cls is not None:
                # # Older version of code to satisfy AirBnb MySQL project
                # module = importlib.import_module("models." +
                #       self.__module_names[cls])
                # class_ = getattr(module, cls)
                # rows = self.__session.query(class_).all()

                # for row in rows:
                #     key = str(cls + "." + row.id)
                #     output[key] = row

                # # Newer ver of code to satisfy AirBnb Web framework
                rows = self.__session.query(cls).all()
                for row in rows:
                    key = str(cls.__name__ + "." + row.id)
                    output[key] = row
            else:
                for class_name, namespace in self.__module_names.items():
                    module = importlib.import_module("models." + namespace)
                    class_ = getattr(module, class_name)
                    rows = self.__session.query(class_).all()

                    for row in rows:
                        key = str(class_name + "." + row.id)
                        output[key] = row

        return output

    def new(self, obj):
        """Add new object to session"""
        if self.__session is not None and obj is not None:
            self.__session.add(obj)

    def save(self):
        """Commit changes for current session"""
        if self.__session is not None:
            self.__session.commit()

    def delete(self, obj=None):
        """Delete object from session"""
        if self.__session is not None:
            if obj is not None:
                self.__session.delete(obj)

    def reload(self):
        """Recreate everything"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close current session"""
        self.__session.close()
        