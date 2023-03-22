#!/usr/bin/python3
''''''
import os
from sqlalchemy import create_engine

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = self.__engine
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')

    all(self, cls=None):

