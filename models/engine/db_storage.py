#!/usr/bin/python3

"""Module that sets up DBstorage using SQLAlchemy"""
import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DB storage for database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """makes an instance"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getnenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                user, password, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects depending
    on the class name (argument cls). If cls=None, query all types
    of objects (User, State, City, Amenity, Place and Review).

    Returns:
        A dictionary of all objects queried, where each key is the
        "<class-name>.<object-id>" string and the value is the object.
    """
        objects_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = setattr(models, cls)
            objects = self.__session.query(cls).all()
        else:
            for cls in names_classes.values():
                objects += self.__session.query(cls).all()
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects_dict[key] = obj
        return objects_dict

    def new(self, obj):
        """Adds an object to the database session"""
        self.__session.add(obj)

    def save(self):
        """Saves an object to the database sesssion"""
        self.__sesssion.commit()

    def delete(self, obj=None):
        """Deletes an ovject from the database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and a new session"""
        Base.metadata.create_all(engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
