#!/usr/bin/python3
"""Datebase storage Engine class"""

import os
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship


class DBStorage:
    """class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(os.getenv("HBNB_MYSQL_USER"),
                                             os.getenv("HBNB_MYSQL_PWD"),
                                             os.getenv("HBNB_MYSQL_HOST"),
                                             os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """

        objDict = {}

        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for cls in [User, State, City, Amenity, Place, Review]:
                objects.extend(self.__session.query(cls).all())

        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objDict[key] = obj
        return objDict

    def new(self, obj):
        """To add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """To commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """To create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = \
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()
