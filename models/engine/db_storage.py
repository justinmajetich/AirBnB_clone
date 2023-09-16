#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import Base, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """Class Docs"""
    __engine = None
    __session = None

    def __init__(self):
        """Function Docs"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}', pool_pre_ping=True)

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None):
        """
        Args:
            cls (_type_, optional): _description_. Defaults to None.
        """
        result = {}
        if cls:
            for obj in self.__session.query(cls).all():
                ClassName = obj.__class__.__name__
                id = obj.id
                KeyName = ClassName + "." + id
                result[keyName] = obj
        else:
            for obj in self.__session.query.all():
                ClassName = obj.__class__.__name__
                id = obj.id
                KeyName = ClassName + "." + id
                result[keyName] = obj
        return result

