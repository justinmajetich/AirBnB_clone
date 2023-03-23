#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from os import getenv
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage:
    """ DataBase Storage """

    __engine = None
    __session = None

    def __init__(self):
        """ initializes connection to database"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST", default="localhost"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        """

        dictionary = {}

        if cls:
            objs = self.__session.query(cls)

        else:
            objs = self.__session.query(
                User, State, City, Amenity, Place, Review)

        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            dictionary[key] = obj

        return dictionary

    def new(self, obj):
        """ add the object to the current database session (self.__session) """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
