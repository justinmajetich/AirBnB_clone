#!/usr/bin/python3
    """Module that houses the database storage engine
    """

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ

running_environment = environ["HBNB_ENV"]
user = environ["HBNB_MYSQL_USER"]
pw = environ["HBNB_MYSQL_PWD"]
host = environ["HBNB_MYSQL_HOST"]
db = environ["HBNB_MYSQL_DB"]
connect_script = f"mysql+mysqldb://{user}:{pw}@{host}:3306/{db}"

class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(connect_script, pool_pre_ping=True)
        if running_environment == "test":
            Base.metadata.drop_all(self.__engine)
