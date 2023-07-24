#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os

class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create engine and link to MySQL database"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query current database session for all objects of given class"""
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for c in classes:
                objs += self.__session.query(c)
        else:
            objs = self.__session.query(cls)
        obj_dict = {str(obj.id): obj for obj in objs}
        return obj_dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in database and create new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute (self.__session)"""
        self.__session.remove()
