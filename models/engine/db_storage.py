#!/usr/bin/python3
''' DBSTORAGE '''

import os
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.orm import scoped_session


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST')
        db_database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f"mysql+mysqldb://{db_user}:{db_pwd}@\
                {db_host}/{db_database}",
            pool_pre_ping=True, echo=True)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        stmt = None
        if cls is None:
            stmt = select()
            return self.__session.scalar(stmt)
        else:
            stmt = select(cls)
        return self.__session.scalar(stmt)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """ to delete obj from __objects """
        if obj is None:
            return

        self.__session.delete(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)

