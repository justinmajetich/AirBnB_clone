#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.user import User
from models.place import Place
from models.state import State
from models.city import Cityhttps://www.google.com/ 
from models.amenity import Amenity
from models.review import Review


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
        if env = 'test':
            Base.metadata.drop_all(self.__engine)


    def all (self, cls=None):
        " Return dictionary of all the objects in the file "


    def new(self, obj):
        " add the object to the current database session "
        self.__session.add(obj)


    def save(self):
        " Commit all changes of hte current database session "
        self.__session.commit(obj)

    def delete(self, obj=None):
        " delete form the current database session"
        if obj is not None:
            __session.delete(obj)

    def reload(self):
        " Create all tables in the database, and creates the current session "
