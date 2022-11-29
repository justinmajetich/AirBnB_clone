#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from sqlalchemy.schema import MetaData


class DBStorage:
    """This class manages dbstorage for hbnb clone"""
    __engine = None
    __session = None

    def __init__(self):
        """ initialize DBStorage class"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              pwd,
                                              host,
                                              db),
                                      pool_pre_ping=True)
        if env == 'test':
            MetaData.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """initialize all method"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        my_dict = {}
        if cls is not None:
            list_obj = self.__session.query(cls).all()
            for obj in list_obj:
                my_dict[f"{obj.__class__}.{obj.id}"] = obj
        else:
            cls_list = [User, State, City, Amenity, Place, Review]
            for cls in cls_list:
                list_obj = self.__session.query(cls).all()
                for obj in list_obj:
                    my_dict[f"{obj.__class__}.{obj.id}"] = obj

    def new(self, obj):
        """add the object tp the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables + create current database session"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self__session = Session()
