#!/usr/bin/python3
"""
module for db storage class
"""
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """The class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for the class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      os.environ.get("HBNB_MYSQL_USER"),
                                      os.environ.get("HBNB_MYSQL_PWD"),
                                      os.environ.get("HBNB_MYSQL_HOST"),
                                      os.environ.get("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            objects = []
            for c in classes:
                objects += self.__session.query(c).all()
        else:
            objects = self.__session.query(cls).all()
        return {type(obj).__name__ + "." + obj.id: obj for obj in objects}

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
