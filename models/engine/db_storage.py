#!/usr/bin/python3
"""Database storage"""
from sqlalchemy import create_engine as create
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import Session
from models.base_model import Base
from os import getenv as env
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class DBStorage():
    '''DBStorage'''

    __engine = None
    __session = None

    def __init__(self):
        '''__init__'''
        test = env('HBNB_ENV')
        self.__engine = create('mysql+mysqldb://{}:{}@{}/{}'.format( \
                                    env('HBNB_MYSQL_USER'),
                                    env('HBNB_MYSQL_USER'),
                                    env('HBNB_MYSQL_USER'),
                                    env('HBNB_MYSQL_USER'),
                                    pool_pre_pring=True))
        if test == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        '''all'''
        new_dict = {}
        objs = []

        if cls == None:
            objs += (self.__session.query(User).all())
            objs += (self.__session.query(City).all())
            objs += (self.__session.query(State).all())
            objs += (self.__session.query(Amenity).all())
            objs += (self.__session.query(Place).all())
            objs += (self.__session.query(Review).all())
        else:
            objs = self.__session.query(cls).all()
        for obj in objs:
            key = obj.to_dict()['__class__'] + '.' + obj.to_dict()['id']
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        '''new'''
        self.__session.add(obj)

    def save(self):
        '''save'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete'''
        #delete from current db session obj if not None
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        '''reload'''
        #create tables in db
        #create current db session using sessionmaker
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine,expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
