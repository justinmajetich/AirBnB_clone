#!/usr/bin/python3
"""DB storage
"""
import models
from models.base_model import BaseModel, Base
from models import city, state
from os import environ, getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """database storage for mysql conversion
    """
    __engine = None
    __session = None

    def __init__(self):
        """initializer for DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        env = getenv("HBNB_ENV")
        if (env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current session and list all instances of cls
        """
        result = {}
        if cls:
            for row in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, row.id)
                row.to_dict()
                result.update({key: row})
        else:
            for table in models.dummy_tables:
                cls = models.dummy_tables[table]
                for row in self.__session.query(cls).all():
                    key = "{}.{}".format(cls.__name__, row.id)
                    row.to_dict()
                    result.update({key: row})
        return result

    def rollback(self):
        """rollback changes
        """
        self.__session.rollback()

    def new(self, obj):
        """add object to current session
        """
        self.__session.add(obj)

    def save(self):
        """commit current done work
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from session
        """
        if (obj is None):
            self.__session.delete(obj)

    def reload(self):
        """reload the session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Scope = scoped_session(Session)
        self.__session = Scope()

    def close(self):
        """display our HBNB data
        """
        self.__session.__class__.close(self.__session)
        self.reload()
