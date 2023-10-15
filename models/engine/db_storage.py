#!/usr/bin/python3
""" The engine for airbnb"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """Class for mysql data storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Class constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB'),
                                             pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classdb_dict = {}
        classes = {"State": State,
                   "City": City,
                   "User": User,
                   "Place": Place,
                   "Review": Review}
        if cls is None:
            for key, value in classes.items():
                query_list = self.__session.query(value).all()
                for obj in query_list:
                    classdb_dict[obj.__class__.__name__ + "." + str(
                        obj.id)] = obj
        else:
            query_list = self.__session.query(cls).all()
            for obj in query_list:
                classdb_dict[obj.__class__.__name__ + "." + obj.id] = obj
        return classdb_dict

    def new(self, obj):
        self.__session.add(obj)  # REVISAR

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):  # REVISAR NUEVO
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
