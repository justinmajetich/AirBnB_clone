#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from os import environ


class DBStorage:
    """ Storage for database with SQL Alchemy and MySQL """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor """

        sqlUser = environ.get('HBNB_MYSQL_USER')
        sqlPwd = environ.get('HBNB_MYSQL_PWD')
        sqlHost = environ.get('HBNB_MYSQL_HOST')
        sqlDb = environ.get('HBNB_MYSQL_DB')
        sqlEnv = environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(sqlUser, sqlPwd, sqlHost, sqlDb),
                                      pool_pre_ping=True)

        if sqlEnv == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        """

        session = self.__session
        dic = {}
        if not cls:
            tables = [User, State, City, Amenity, Place, Review]

        else:
            if type(cls) == str:
                cls = eval(csl)

            tables = [cls]

        for t in tables:
            query = session.query(t).all()

            for rows in query:
                key = "{}.{}".format(type(rows).__name__, rows.id)
                dic[key] = rows

        return dic

    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from module import symbol
        the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        creates all tables in the database
        creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Closes Session
        """
        self.__session.close()
