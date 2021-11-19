#!/usr/bin/python3
"""defines a class to manage database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


class DBStorage:
    """Class for database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the storage"""
        usr = getenv(HBNB_MYSQL_USER)
        pwd = getenv(HBNB_MYSQL_PWD)
        host = getenv(HBNB_MYSQL_HOST)
        db = getenv(HBNB_MYSQL_DB)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            usr, pwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
