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
        " Delete table is env value is 'test'"
        if env = 'test':
            .drop()


    def all (self, cls=None):
        " Return dictionary of all the objects in the file "


    def new(self, obj):
        " add the object to the current database session "


    def save(self):
        " Commit all changes of hte current database session "


    def delete(self, obj=None):
        " delete form the current database session"

    def reload(self):
        " Create all tables in the database, and creates the current session "
