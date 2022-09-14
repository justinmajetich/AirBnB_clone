#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB"),
                                             pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.create_all(self.__engine)
