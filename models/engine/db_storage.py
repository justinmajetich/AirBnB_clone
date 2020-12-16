#!/usr/bin/python3
"""DB Storage to save in MySQL
"""
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ DBs class """
    __engine = None
    __session = None

    def __init__(self):
        """Variables to DBStorage"""
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(username,
                                              password,
                                              host,
                                              db_name),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Objects that depending of the class name"""

        dictionary = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            _query = self.__session.query(User, State, City, Amenity,
                                          Place, Review)

            for obj in _query:
                key_obj = ("{}.{}".format(obj.__class__.__name__, obj.id))
                dictionary.update({key_obj: obj})
            return dictionary
        else:
            if cls in classes:
                _query = self.__session.query(cls).all()
                for obj in _query:
                    key_obj = ("{}.{}".format(obj.__class__.__name__, obj.id))
                    dictionary.update({key_obj: obj})
                return dictionary
            else:
                return {}

    def new(self, obj):
        """New object in database"""
        self.__session.add(obj)

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete objetc from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creating all tables"""
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
        ))
        self.__session = Session()
