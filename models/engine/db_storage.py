#!/usr/bin/python3
"""Database file storage"""
import os
from sqlalchemy import create engine
from sqlalchemy.orm import Session

class DBStorage:
    """Define a database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializer"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get("HBNB_MYSQL_USER"),
            os.environ.get("HBNB_MYSQL_PWD"),
            os.environ.get("HBNB_MYSQL_HOST", "localhost"),
            os.environ.get("HBNB_MYSQL_DB")), pool_pre_ping=True)

        with Session(self.__engine):
            
