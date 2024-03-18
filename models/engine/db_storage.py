#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User


class DBStorage:
    """This class defines the database storage engine"""

    __engine = None
    __session = None
    __models = [State, City, User]

    def __init__(self):
        """Instantiates a new DBStorage object."""
        self.__engine = create_engine(
            "mysql+mysqldb://"
            f"{getenv('HBNB_MYSQL_USER')}:{getenv('HBNB_MYSQL_PWD')}"
            f"@{getenv('HBNB_MYSQL_HOST')}/{getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True,
        )

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects in the current
        database session."""
        objects = {}

        if cls:
            for obj in self.__session.query(cls).all():
                objects[obj.__class__.__name__ + "." + obj.id] = obj
        else:
            for model in self.__models:
                for obj in self.__session.query(model).all():
                    objects[obj.__class__.__name__ + "." + obj.id] = obj

        return objects

    def new(self, obj):
        """Adds the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and the current
        database session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        db_session = scoped_session(session_factory)
        self.__session = db_session()
