#!/usr/bin/python3
""" DBStorage Module """

from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

classes = {'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review}


class DBStorage:
    """Serializes instances to a database and deserializes from the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine and link to the database"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        a_dict = {}
        if cls is None:
            for value in classes.values():
                for o in self.__session.query(value):
                    k = o.__class__.__name__ + '.' + o.id
                    a_dict[k] = o
        if cls in classes:
            for o in self.__session.query(classes[cls]):
                k = o.__class__.__name__ + o.id
                a_dict[k] = o
        return a_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()
