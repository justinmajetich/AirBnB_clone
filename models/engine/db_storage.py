#!/usr/bin/python3
"""This module defines class DBStorage for database storage engine"""
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import text
import os


class DBStorage:
    """
    Args:
        __engine(db engine): engine for mysql
        __session(Session): instantiates a session for the database
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a mysql database engine and scoped session"""

        USER = os.getenv("HBNB_MYSQL_USER")
        PWD = os.getenv("HBNB_MYSQL_PWD")
        HOST = os.getenv("HBNB_MYSQL_HOST")
        DB = os.getenv("HBNB_MYSQL_DB")
        environment = os.getenv("HBNB_ENV")

        # dialect -> mysql, driver -> mysqldb
        URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(USER, PWD, HOST, DB)
        # create database engine
        self.__engine = create_engine(URL, pool_pre_ping=True)

        if environment == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None) -> dict:
        """
        Queries the current database session based on the class name (cls).
        If cls is None, then all types of Objects are queried i.e
        User, State, City, Amenity, Place and Review.
        """
        all_dict = {}
        # classes = [Amenity, City, Place, Review, State, User]
        classes = [City, State, User, Place]
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            cls_rows = self.__session.query(cls)
            for row in cls_rows:
                key = "{}.{}".format(type(row).__name__, row.id)
                all_dict[key] = row

        else:
            for cls_name in classes:
                query_all_rows = self.__session.query(cls_name)
                for row in query_all_rows:
                    key = "{}.{}".format(type(row).__name__, row.id)
                    all_dict[key] = row
        return all_dict

    def new(self, obj):
        """Adds the object (obj) to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session"""
        self.__session.commit()
        # self.__session.close()

    def delete(self, obj=None):
        """
        Deletes object obj from the current database session
        if obj is not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and creates the
        current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
