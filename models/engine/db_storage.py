#!/usr/bin/python3
"""This is a DBStorage class for AirBnB"""
import os

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """MySQL database storage engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """Connect to a database and initiate a session
        """
        url = {
            'drivername': 'mysql+mysqldb',
            'username': os.getenv('HBNB_MYSQL_USER', 'hbnb_dev'),
            'password': os.getenv('HBNB_MYSQL_PWD', 'hbnb_dev_pwd'),
            'host': os.getenv('HBNB_MYSQL_HOST', 'localhost'),
            'port': os.getenv('HBNB_MYSQL_PORT', 3306),
            'database': os.getenv('HBNB_MYSQL_DB', 'hbnb_dev_db'),
        }
        self.__engine = create_engine(URL(**url), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Get a dictionary of all objects
           Return:
           returns a dictionary of objects
        """
        if cls is None:
            classes = {Amenity, City, Place, Review, State, User}
            return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                    for res in map(self.__session.query, classes)
                    for obj in res}
        else:
            return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                    for obj in self.__session.query(cls)}

    def new(self, obj):
        """Add an object to the session
           Args:
           obj: given object
        """
        if obj:
            self.__session.add(obj)

    def delete(self, obj=None):
        """Delete an object from the session
        """
        if obj:
            self.__session.delete(obj)

    def save(self):
        """Save changes made this session
        """
        self.__session.commit()

    def reload(self):
        """Create all tables and load database
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def close(self):
        """Close the session reload
        """
        self.__session.close()
