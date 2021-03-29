#!/usr/bin/python3
""" DBS storage module for mysqlalchemy """
from sqlalchemy import create_engine
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """ DBS Storage """
    __engine = None
    __session = None
    
    def __init__(self):
        """ sets up stroage engine class with given env variables """
        usr = getenv("HBNB_MYSQL_USER")
        paswd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(usr, paswd, host, db), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Runs a query that returns a dictionary of objects"""
        return_dict = {}
        class_list = [State, City, User, Place, Review]
        if (cls is not None):
            results = self.__session.query(cls).all()
            for obj in results:
                return_dict["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj
        else:
            for cls_obj in class_list:
                results = self.__session.query(cls_obj).all()
                for obj in results:
                    return_dict["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj
        return return_dict

    def new(self, obj):
        """ adds a new object to sessions """
        self.__session.add(obj)

    def save(self):
        """ commits changes to table """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes a given object from table """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reloads all tables with new session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
