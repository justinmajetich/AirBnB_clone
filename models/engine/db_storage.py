#!/usr/bin/python3
"""Database storage engine module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ """
        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

        cls_dict = {}
        if cls in classes:
            list_obj = self.__session.query(cls).all()
        elif cls is None:
            list_obj = []
            for item in classes:
                list_obj += self.__session.query(item).all()
        for obj in list_obj:
            cls_dict[f"{cls.__name__}.{obj.id}"] = obj
        return cls_dict

    def new(self, obj):
        """ Adds object to current db session"""
        self.__session.add(obj)

    def save(self):
        """ Commits changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current db session"""
        if obj:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """Creates all tables in the db and creates the current db sesh"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
