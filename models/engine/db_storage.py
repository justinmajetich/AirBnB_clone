#!/usr/bin/python3

"""This module defines a ``DBStorage`` class
for the MySQL storage option for the Airbnb clone
"""
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.base_model import BaseModel, Base
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Defines the MySQL database storage class"""

    __engine = None
    __session = None
    __valid_classes = {
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review,
    }

    def __init__(self):
        """Initializes a ``DBStorage`` class instance

        Atributes:
        """
        dev_environ = getenv("HBNB_ENV", "Please set environment")
        user = getenv("HBNB_MYSQL_USER", "Please set user")
        password = getenv("HBNB_MYSQL_PWD", "Please set password")
        host = getenv("HBNB_MYSQL_HOST", "Please set host")
        database = getenv("HBNB_MYSQL_DB", "Please set database")
        port = 3306

        url = f"mysql+mysqldb://{user}:{password}@{host}:{port}/{database}"
        self.__engine = create_engine(url, pool_pre_ping=True)

        if dev_environ == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all instances of all the classes
        in the database, or of a class, if specified"""

        db_storage = []

        if not issubclass(cls, BaseModel):
            raise TypeError(f"{cls} is not a subclass of BaseModel")

        if cls and cls in DBStorage.__valid_classes.values():
            db_storage = self.__session.query(cls).all()
        else:
            for cls in DBStorage.__valid_classes.values():
                db_storage.extend(self.__session.query(cls).all())

        return {"{}.{}".format(type(obj).__name__, obj.id): obj
                for obj in db_storage}

    def new(self, obj):
        """Adds an object to the current database session """
        if isinstance(obj, BaseModel):
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all the tables from the MySQL database"""
        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
