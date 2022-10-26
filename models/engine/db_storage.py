#!/usr/bin/python3
""" This module defines a class to manage database storage for airbnb clone """

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:
    """ blank """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initalize DB Storage object
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """
        Query on current database session objects depending on class name
        """
        query_dict = {}
        cls_dict = {}
        classes = {User, State, City, Amenity, Place, Review}
        if cls in classes:
            cls_dict = self.__engine.query(cls).all()

        if cls == None:
            for cls_name in classes:
                cls_dict.update(self.__engine.query(cls_name).all())
        
        for obj in cls_dict:
            key = obj.__class__.__name__ + obj.id
            query_dict[key] = obj
        
        return query_dict

    def reload(self):
        """
        
        """
        Base.metadata.create_all(engine)