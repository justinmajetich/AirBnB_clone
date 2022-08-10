#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from os import getenv

user = getenv(HBNB_MYSQL_USER)
passwd = getenv(HBNB_MYSQL_PWD)
host = getenv(HBNB_MYSQL_HOST)
db = getenv(HBNB_MYSQL_DB)
env = getenv(HBNB_ENV)


class DBStorage():

        __engine = None
        __session = None


    def __init__(self):
        __engine = self.__engine
        __engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    format(user, passwd, host, db), pool_pre_ping=True)

        def drop():
            if env = 'test':
                .drop()
