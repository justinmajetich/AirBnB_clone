#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    This class manages storage of the AirBnB clone project in MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage """
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        env = os.environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Query all objects from the current database session based on class name
        If cls=None, return all types of objects
        """
        obj_dict = {}
        if cls is None:
            cls_list = [State, City, User, Place, Review, Amenity]
        else:
            cls_list = [cls]

        for c in cls_list:
            query = self.__session.query(c)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """
        Add obj to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database (feature of SQLAlchemy)
        Create current database session using a sessionmaker with option
        expire_on_commit=False, scoped_session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Calls remove() on the private session attribute or
        close() on the class Session
        """
        self.__session.close()