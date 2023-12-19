#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True
            )
        )
        if os.getenv(HBNB_ENV) == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query the DB"""
        if cls is not None:
            return DBStorage.__session.query(cls).all()
        return 
