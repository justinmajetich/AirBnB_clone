#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    """Stablishing connection with a sql database
    """

    __engine = None
    __session = None


    def __init__(self):
        """Instantiate an Object of DBStorage"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}'
        )
