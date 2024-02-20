#!/usr/bin/python3

"""
    Module: db_storage
    Database storage engine
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os


class DBStorage:
    """
    DBStorage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        """
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session all objects depending of the
        class name """
        objects = {}
        if cls:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            
            for obj in self.__session.query(User):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
            for obj in self.__session.query(State):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
            for obj in self.__session.query(City):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
            for obj in self.__session.query(Place):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
            for obj in self.__session.query(Review):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
            for obj in self.__session.query(Amenity):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj=None)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """"Close the current session"""
        self.__session.close()
    