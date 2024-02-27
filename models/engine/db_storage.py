#!/usr/bin/python3
"""New engine DBStorage"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Class that manages DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on database session"""