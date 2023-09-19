#!/usr/bin/python3
"""Defines the DBStorage class."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City

class DBStorage:
    """Represents the database storage engine.
    Attributes:
        __engine (sqlalchemy.engine.base.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.orm.session.Session): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new DBStorage instance."""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session for all objects of class cls.
        Returns a dictionary of the objects with their IDs as keys.
        If cls is None, queries all types of objects.
        """
        classes = [State, City]
        objects = {}
        if cls is None:
            for cl in classes:
                for obj in self.__session.query(cl):
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objects[key] = obj
        else:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds the object obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and initializes a session."""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """Closes the working SQLAlchemy session."""
        self.__session.remove()

