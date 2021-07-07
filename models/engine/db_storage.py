#!/usr/bin/python3
"""new storage"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage():
    """new storge"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization of DBStorage"""
        MYSQL_USER = getenv('HBNB_MYSQL_USER')
        MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        MYSQL_DB = getenv('HBNB_MYSQL_DB')
        MYSQL_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(MYSQL_USER,
                                              MYSQL_PWD,
                                              MYSQL_HOST,
                                              MYSQL_DB), pool_pre_ping=True)
        if MYSQL_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session
        all objects depending of the class name"""
        result_dict = {}
        for itr in classes:
            if cls is None or itr == cls:
                list_objs = self.__session.query(classes[itr]).all()
                for obj in list_objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    result_dict[key] = obj
        return (result_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)
        self.save()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload method for db session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """remove and close the session"""
        self.__session.close()
