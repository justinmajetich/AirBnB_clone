#!usr/bin/python3
"""
Module documentation
"""
from sqlalchemy import create_engine
from os import getenv
from models import Base

class DBStorage:
    """
    Class's documentation
    """
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}', pool_pre_ping=True)

        if (env == "test"):
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass
