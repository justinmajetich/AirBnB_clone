#!/usr/bin/python3
"""
Database Storage Engine Module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {'User': User, 'Place': Place,
           'State': State, 'City': City,
           'Review': Review, 'Amenity': Amenity
           }


class DBStorage:
    """
    Database Storage Class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiate the DBStorage class
        """
        # Get environmental variables
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query current database session for all objects of class
        """

        object_dict = {}

        if cls is not None:
            for obj in self.__session.query(cls).all():
                object_dict.update({'{}.{}'.format(type(cls).__name__,
                                                   obj.id): obj})
        else:
            for name in classes.values():
                object_list = self.__session.query(name)
                for obj in object_list:
                    object_dict.update({'{}.{}'.format(type(obj).__name__,
                                                       obj.id): obj})
        return object_dict

    def new(self, obj):
        """
        Adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete object from current database if obj is not None
        """
        if obj is not None:
            self.__session.delete(obj)
        else:
            pass

    def reload(self):
        """
        Create all tables in the database
        Create current database session
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """
        End attributes
        """
        self.__session.remove()
