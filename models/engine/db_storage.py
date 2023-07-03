#!/usr/bin/python3
"""Defines the DBStorage engine."""

import os
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from models.base_model import Base


class DBStorage:
    """Database Storage Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        # Get environmental variables
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
