#!/usr/bin/python3
""" Modules for DBstorage """
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
import models


class DBStorage:
    """ Class for the DB """
    __engine = None
    __session = None

    def __init__(self):
        """ attrs of storage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the current database session"""
        o_d = dict()
        if cls is None:
            listClasses = [Amenity, City, Place, State, Review, User]
            for class_ in listClasses:
                try:
                    query = self.__session.query(class_).all()
                    for object_ in query:
                        className = object_.to_dict()['__class__']
                        id_ = object_.id
                        c_id = className + "." + id_
                        o_d[c_id] = object_
                except Exception:
                    pass
        else:
            query = self.__session.query(cls).all()
            for object_ in query:
                className = object_.to_dict()['__class__']
                id_ = object_.id
                c_id = className + "." + id_
                o_d[c_id] = object_
        return o_d

    def new(self, obj):
        """ add obj in the DB """
        self.__session.add(obj)

    def save(self):
        """ Commit in the DB """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Remove or close the session """
        self.__session.close()
