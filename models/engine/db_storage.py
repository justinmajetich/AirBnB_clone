#!/usr/bin/python3
"""Database Storage for AirBnB_clone project"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
classes = [User, State, City, Place, Review, Amenity]


class DBStorage:
    """class that represents Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns all objects of cls (if not none),
        otherwise returns all objects.
        """
        dic_t = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dic_t[key] = obj
        else:
            for clss in classes:
                objss = self.__session.query(clss)
                for obj in objss:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dic_t[key] = obj
        return dic_t

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the current database session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
