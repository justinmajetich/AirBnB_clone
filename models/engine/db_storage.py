#!/usr/bin/python3
"""a script for DB Storage Engine"""
import os
from sqlalchemy import Base
from sqlalchemy import create_engine

# retrieve DB credentials using env variables
user = os.getenv('HBNB_MYSQL_USER')
password = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
database = os.getenv('HBNB_MYSQL_DB')
env = os.getenv("HBNB_ENV")


class DBStorage():
    """create the engine to be linked to the MySQL
    database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of engine"""
        db_url = "mysql+mysqldb://user:password@host/database, , pool_pre_ping=True"
        engine = create_engine(db_url)
        self.__engine = engine(db_url)
        if env == 'test':
            Base.metadata.drop_all(engine)
