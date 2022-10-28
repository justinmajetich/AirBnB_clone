#!/usr/bin/python3
"""
the Database storage module
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage:
    """The Database Storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initializing the DBStorage objects"""
        self.__engine = create_engine('mysql+mysqldb://'
                                      f'{getenv("HBNB_MYSQL_USER")}:'
                                      f'{getenv("HBNB_MYSQL_PWD")}@'
                                      f'{getenv("HBNB_MYSQL_HOST")}/'
                                      f'{getenv("HBNB_MYSQL_DB")}',
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on all objects of a class or all classes"""
        obj_dict = {}
        if cls:
            cls_objs = self.__session.query(cls).all()
            for obj in cls_objs:
                obj_dict.update({cls + '.' + obj.id: obj})
            return obj_dict
        else:
            cls_objs = self.__session.query(User, State, City, Amenity,
                                            Place, Review).all()
            for obj in cls_objs:
                obj_dict.update({obj.__class__.__name__ + '.' + obj.id: obj})
            return obj_dict

    def new(self, obj):
        """add new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from the current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables and ensures secure threading"""
        self.__session = scoped_session(sessionmaker()(bind=self.__engine,
                                        expire_on_commit=False))
        Base.metadata.create_all(self.__engine)