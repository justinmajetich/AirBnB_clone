#!/usr/bin/python3
"""
    New engine DB storage
"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import Base


class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None


    def __init__(self):
        """DBStorage instantiation method"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
                            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                 user, passwd, host, db),
                             pool_pre_ping=True)
