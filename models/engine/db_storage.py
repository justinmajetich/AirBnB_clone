#!/usr/bin/python3
""" This module represents the Database engine """
from lib2to3.fixes import fix_itertools_imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from os import environ

user = environ.get("HBNB_MYSQL_USER")
pwd = environ.get("HBNB_MYSQL_PWD")
host = environ.get("HBNB_MYSQL_HOST")
env = environ.get("HBNB_ENV")
db = environ.get("HBNB_MYSQL_DB")

Base = declarative_base()


class DBStorage(Base):
    """ Database Storage Class """
    __engine = None
    __session= None

    def __init__(self):
        """ Instantiates new object """
        self.__engine = create_engine(f"mysql+mysqldb://{user}\
        :{pwd}@{host}", pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Makes a query on the current database session """

