#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

from models import *
from sqlalchemy import create_engine
from os import getenv

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')


class DBStorage:
    """This class manages db storage of hbnb models in JSON format"""
    __engine = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST, HBNB_MYSQL_DB)
                )
