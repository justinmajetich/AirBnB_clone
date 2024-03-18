#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy import (create_engine)
import os
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


hbnb_dev = os.getenv('HBNB_MYSQL_USER')
hbnb_dev_pwd = os.getenv('HBNB_MYSQL_PWD')
localhost = os.getenv('HBNB_MYSQL_HOST')
hbnb_dev_db = os.getenv('HBNB_MYSQL_DB')
hbnb_environ = os.getenv('HBNB_ENV')

class DBStorage():
    """This defines the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(hbnb_dev, hbnb_dev_pwd,
                                              localhost, hbnb_dev_db),
                                              pool_pre_ping=True)
        if hbnb_environ == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is not None:
            classes = [cls]
        else:
            classes = [User, State, City, Amenity, Place, Review]
        new_dict = {}
        for each_cls in classes:
            for obj in self.__session.query(each_cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
