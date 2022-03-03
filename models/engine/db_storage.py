#!/usr/bin/python3
"""This module defines a class to manage file storage for using a database
"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session, scoped_session
from importlib_metadata import metadata


class DBStorage:
    """This class manages storage of hbnb models in SQL format
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates Instance into DBStorage using env vars
        """
        dialect = "mysql"
        driver = "mysqldb"
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine('{}+{}://{}:{}@{}/{}'
                                .format(dialect, driver, user, passwd, host,
                            db), pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

