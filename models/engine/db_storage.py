#!/usr/bin/python3
"""Defines the DBStorage class."""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
        DBStorage model
        Attributes: 
            __engine
            __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a the DBStorage instance."""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ show all databases object"""
        objects = {}

        if cls is None:
            classes = [User, State, City, Place, Amenity, Review]
            query_objs = []

            for clss in classes:
                query_objs.extend(self.__session.query(clss).all())
        else:
            query_objs = self.__session.query(cls).all()

        for obj in query_objs:
            class_name = obj.__class__.__name__
            key_name = f"{class_name}.{obj.id}"
            objects[key_name] = obj

        return objects

    def new(self, obj):
        """Create new object in the current database session."""
        self.__session.add(obj)

    def save(self):
        """save changes for the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object instance from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and initializes a session."""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()

    def close(self):
        """Closes the SQLAlchemy session."""
        self.__session.remove()

