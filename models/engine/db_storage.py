#!/usr/bin/python3
""" db storage """

from os import getenv
from models.base_model import Base
import sqlalchemy import create_engine


class DBStorage:
    """ db storage """

    __engine = None
    __session = None


    def __init__(self):
        ''' init '''

        db_user = getenv('HBNB_MYSQL_USER')
        db_user = getenv('HBNB_MYSQL_PWD')
        db_user = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV') 

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                      db_user, db_pass, db_host, db), 
                                      pool_pre_ping=True) 
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        ''' reload '''
        from sqlalchemy.orm import sessionmaker, scoped_session

        Base.metadata.create_all(self.__engine)
        sess = sm(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def all(self, cls=None):
        ''' all '''
''' next '''

    def new(self, obj):
        ''' new '''

        if obj is None:
            return
        self.__session.add(obj)

    def save(self):
        ''' save '''

        self.__session.commit()

    def delete(self, obj=None):
        ''' delete '''

        if obj is None:
            return
        else:
            self.__session.delete(obj) 
