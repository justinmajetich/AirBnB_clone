#!/usr/bin/python3
"""
This module defines a class to manage
db storage for hbnb clone
"""

from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')


class DBStorage:
    """This class manages db storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True
                )
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database
        session (self.__session) all objects
        depending of the class name (argument cls)
        """
        classes = {'User': User, 'Place': Place,
                   'State': State, 'City': City,
                   'Review': Review}
        obj_dict = {}
        if cls:
            cls_objs = self.__session.query(classes[cls]).all()
        else:
            cls_objs = []
            for cls_name in list(classes.values()):
                cls_obj = self.__session.query(cls_name)
                if cls_obj:
                    cls_objs.extend(cls_obj)

        for obj in cls_objs:
            if "_sa_instance_state" in obj.__dict__.keys():
                del obj.__dict__['_sa_instance_state']
            key = obj.__class__.__name__ + '.' + obj.id
            obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        query on the current database session
        (self.__session) all objects depending
        of the class name (argument cls)
        """

        self.__session.add(obj)

    def reload(self):
        """
        create all tables in the database
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session

    def save(self):
        """
        commit all changes of the current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
         Delete from the current database
         session obj if not None
        """

        if obj:
            self.__session.delete(obj)
