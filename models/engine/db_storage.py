#!/usr/bin/python3
"""Class DBStorage"""

import models
from os import getenv
from sqlalchemy import create_engine


class DBStorage:
    """Class for interacting with the database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize instance of DBStorage"""

        # Get environmental variables
        user = getenv(HBNB_MYSQL_USER)
        password = getenv(HBNB_MYSQL_PWD)
        host = getenv(HBNB_MYSQL_HOST)
        database = getenv(HBNB_MYSQL_DB)

        #start engine
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}\
                                      @{host}/{database}', pool_pre_ping=True)

        #check if test
        if getenv(HBNB_ENV) == "test":
            pass # drop all tables

    def all(self, cls=None):
        """Query current DB for all objects of class (cls)"""
