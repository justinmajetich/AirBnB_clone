#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os import getenv
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

usr = getenv('HBNB_MYSQL_USER')
pwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')
dbtables = [State, City, User]


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage constructor"""
        self.__engine = DBStorage.connection()
        if (env == 'test'):
            Base.metadata.drop_all(self.engine)

    @staticmethod
    def connection():
        """Connection to database function"""
        conn = 'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db)
        return create_engine(conn, pool_pre_ping=True, echo=False)

    def all(self, cls=None):
        """query on the current database session"""
        rdict = {}
        result = []
        if (cls is None):
            for t in dbtables:
                result.extend(self.__session.query(t).all())
        else:
            result = self.__session.query(cls).all()
        for obj in result:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            rdict[key] = obj
        return rdict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object if exists in current db session"""
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        presession = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(presession)
        self.__session = Session()
