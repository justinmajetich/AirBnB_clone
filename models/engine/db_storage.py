#!/usr/bin/python3
"""Defines the class DBStorage"""
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session


class DBStorage:
    """Representes a class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """initialize the instance of DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects
        depending of the class name.
        """
        all_class = [City, State, User, Place, Review, Amenity]
        obj_list = []
        new_dict = {}

        if cls is None:
            for i in range(len(all_class)):
                obj_list += self.__session.query(all_class[i]).all()
        else:
            obj_list = self.__session.query(cls).all()

        for obj in obj_list:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
