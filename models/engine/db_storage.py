#!/usr/bin/python3
"""
Module db_storage
"""
from sqlalchemy import create_engine
import os
from models.base_model import Base
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None
    def __init__(self):
        """Constructor for DBStorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All function
        all objects depending of the class name
        return a dictionary"""
        self.__session = sessionmaker(self.__engine)
        ses = self.__session()
        

