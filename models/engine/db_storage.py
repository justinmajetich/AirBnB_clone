#!/usr/bin/python3
""" engine DBStorage """
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class DBStorage:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    """ Manage storage in bd """
    __engine = None
    __session = None

    def __init__(self):
        """ init engine ro sqlalchemist """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306/hbnb_dev_db', pool_pre_ping=True)
        if HBNB_ENV == 'tets':
            Base.metadata.drop_all()
        
    def all(self, cls=None):
        """ call all """
        if cls is not None:
            query = self.__session.query(cls)
            for row in query:
                    print('[{}]'.format(row))
            return (query)
        else:
            classes = [State, City, Review, Amenity, Place, User]
            repuesta = []
            for clas in classes:
                query = self.__session.query(clas)
                for row in query:
                    print('[{}]'.format(row))
            return (repuesta)
        
    
    
    def new(self, obj):
        """ add values in table"""
        self.__session.add(obj)

        
    def save(self):
        """ save changes in talbes"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete imput in table"""
        pass

    def reload(self):
        """ recharge session and tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False )
        self.__session = scoped_session(session_factory)
         


