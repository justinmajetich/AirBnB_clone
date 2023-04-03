#!/usr/bin/python3
''' new engine DBSTORAGE'''

import os
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
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
        db_env = os.environ.get("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3307/{}".
                                      format(db_user, db_pwd, db_host, db_database),
                                      pool_pre_ping=True)

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

        if db_env == "test":
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

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
        print(self.__engine)
        Base.metadata.create_all(bind=self.__engine)