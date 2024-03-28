#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ

class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        user = environ['HBNB_MYSQL_USER']
        passwd = environ['HBNB_MYSQL_PWD']
        host = environ['HBNB_MYSQL_HOST']
        db = environ['HBNB_MYSQL_DB']
        env = environ['HBNB_ENV']

        url = f"mysql+mysqldb://{user}:{passwd}@{host}/{db}"
        self.__engine = create_engine(url, pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            q = self.__session.query(cls).all()
        else:
            q = self.__session.query(State).all() + \
                self.__session.query(City).all() + \
                self.__session.query(User).all() + \
                self.__session.query(Place).all()
        return {f"{obj.__class__.__name__}.{obj.id}": obj
                for obj in q}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        """
        Delete an object if it is in the list of objects
        Args:
            obj: The object that will be deleted
        """
        if obj is not None:
            self.__session.delete(obj)

