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

all_classes = {'State': State, 'City': City,
               'User': User, 'Place': Place,
               #'Review': Review, 'Amenity': Amenity
              }


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
        classes = {'User': User, 'State': State,
                   'City': City,# 'Amenity': Amenity,
                   #'Place': Place, 'Review': Review
                   }

    def all(self, cls=None):
        """ """
        obj_dict = {}

        if cls is not None:
            for obj in self.__session.query(cls).all():
                obj_dict.update({f'{type(cls).__name__}.{obj.id}': obj})
        else:
            for class_name in all_classes.values():
                obj_list = self.__session.query(class_name)
                for obj in obj_list:
                    obj_dict.update({f'{type(obj).__name__}.{obj.id}': obj})
        return obj_dict

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
