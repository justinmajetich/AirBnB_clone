#!/usr/bin/python3
"""Database storage engine module"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base

class DBStorage:
    """database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Creates engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, password, host, database), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        if env == "test":
            Base.metadata.drop_all()
