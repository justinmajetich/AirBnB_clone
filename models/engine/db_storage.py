#!/usr/bin/python3
"""
db_storage module
"""
from os import getenv, environ
from models.base_model import BaseModel
from models.


class DBStorage:
    """DB Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                       HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                       HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                       pool_pre_ping=True)
        Base.metadata.create_all(engine)

    def all(self, cls=None):

