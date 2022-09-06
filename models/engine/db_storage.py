#!/usr/bin/python3
"""SQLAlchemy class"""
import json
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ This is DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor method
        """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        envi = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if envi == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return
        A dictionary like in FileStorage
        """
        dicty = {}

        if cls is None:
            list_classes = [State, City, User, Place, Review, Amenity]
            for classes in list_classes:
                query = self.__session.query(classes)
                for items in query.all():
                    key = "{}.{}".format(type(items).__name__, items.id)
                    dicty[key] = items

        else:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for items in query.all():
                key = "{}.{}".format(type(items).__name__, items.id)
                dicty[key] = items

        return(dicty)

    def new(self, obj):
        """Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and
        the current database session
        """
        Base.metadata.create_all(self.__engine)

        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)

        self.__session = Session()

    def close(self):
        """Closes ORM session
        """
        self.__session.close()
