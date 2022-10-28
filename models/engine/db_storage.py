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
            cls_dict = self.__session.query(cls).all()

        if cls is None:
            for cls_name in classes:
                cls_dict.update(self.__session.query(cls_name).all())

        for obj in cls_dict:
            key = obj.__class__.__name__ + obj.id
            query_dict[key] = obj

        return query_dict

    def reload(self):
        """
        Create all tables in database + self.__session attribute
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def new(self, obj):
        """ add object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.session.delete(obj)
