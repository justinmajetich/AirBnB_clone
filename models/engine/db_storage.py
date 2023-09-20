#!/usr/bin/python3
''' Define the DBStorage engine '''
from models.base_model import Base
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        ''' Instantiate the DBStorage Instance '''
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV = 'test':
            Base.metadata.drop_all(self.__engine)
