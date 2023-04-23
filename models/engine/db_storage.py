#!/usr/bin/python3
"""Module for DB storage
   contains the class ``DBStorage`` used to setup
   mysql database storage with sqlalchomy ORM.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base

HBNB_ENV = os.getenv('HBNB_ENV')
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    """DB storage engine setup class"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all
           objects depending of the class name (argument cls)
        """
        result = {}
        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
        return result

    def new(self, obj):
        """Add the object to the current database
           session (self.__session)
        """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()

    def save(self):
        """Commit all changes of the current db session
           (self.__session)
        """
        self.__session.commit()

    def delete(self, obj):
        """delete from the current database session obj
           if not None
        """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """Create all tables in the database (feature of SQLAlchemy).
           Create the current database session (self.__session)
           from the engine (self.__engine) by using a sessionmaker.
            Options:
            expire_on_commit must be set to False
            scoped_session - to make sure your Session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """Close the current running db session"""
        self.__session.close()
