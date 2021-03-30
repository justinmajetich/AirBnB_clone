#!/usr/bin/python3
'''
SQLAlchemy storage engine
'''
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    '''Creates a storage engine and new session'''
    __engine = None
    __session = None

    def __init__(self):
        '''Instantiates an engine'''
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(getenv('HBNB_MYSQL_USER'),
                    getenv('HBNB_MYSQL_PWD'),
                    getenv('HBNB_MYSQL_HOST'),
                    getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            self.__engine.drop_all()

    def all(self, cls=None):
        """queries current db session for all objs depending on cls"""
        objects = {}
        if cls == None:
            for obj in self.__session.query().all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """add obj to current db"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the db and current db session from engine"""
        Base.metadata.create_all(self.__engine)
        session_store = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        our_session = scoped_session(session_store)
        self.__session = our_session()
