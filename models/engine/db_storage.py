#!/usr/bin/python3
"""Model a DBStorage for the HBNB clone"""

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                                getenv("HBNB_MYSQL_USER"),
                                                getenv("HBNB_MYSQL_PWD"),
                                                getenv("HBNB_MYSQL_HOST"),
                                                getenv("HBNB_MYSQL_DB"),
        ), pool_pre_ping=True, )
    
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all types of object and return a dictionary of the object"""
        dictionary = {}
        for all_class in classes:
            if cls is None or cls is classes[all_class] or cls is all_class:
                objs = self.__session.query(classes[all_class]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj
        return dictionary
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes to the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()
    
    def close(self):
        """Calls close() on self._session."""
        self.__session.close()
