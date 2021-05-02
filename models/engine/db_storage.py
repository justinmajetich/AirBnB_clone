#!/usr/bin/python3
"""DBStorage Engine"""
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """Class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects
        Return a dictionary
        """
        class_objects = {}
        if cls is None:
            objects = self.__session.query(User, State, City,  Amenity,
                                           Place, Review)
            for obj in objects:
                key = type(obj).__name__ + "." + str(obj.id)
                class_objects[key] = obj
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = type(obj).__name__ + "." + str(obj.id)
                class_objects[key] = obj

        return class_objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ method used for sesssion closing """
        self.__session.close()
