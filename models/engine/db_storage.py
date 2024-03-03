#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import getenv
from sqlalchemy import create_engine


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        host = getenv("HBNB_MYSQL_HOST")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            pass
