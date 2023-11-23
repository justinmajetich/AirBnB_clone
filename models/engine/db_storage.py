#!/usr/bin/python3
"""
Module defines DBStorage class for HBNB project
"""


from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv


class DBStorage:
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Create new instance of DBStorage
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects of a certain class"""
        objs = {}
        if cls:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objs[key] = obj
        else:
            for table in Base.metadata.tables.keys():
                for obj in self.__session.query(eval(table)):
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """add a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """save all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all objects from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close current session"""
        self.__session.close()
