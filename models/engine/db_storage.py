#!/usr/bin/python3
''' Database Storage '''
import os
from models.base_model import BaseModel, Base
from sqlalchemy import MetaData
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:

    '''
       Database engine for Hbnb
    '''

    __engine = None
    __session = None

    def __init__(self):
        ''' initializes engine '''
        env = os.getenv('HBNB_ENV')
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, db, pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        '''returns dictionary representation of database
           if cls not specified, returns all classes
        '''
        result = {}
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                result[key] = obj
        else:
            for sub_c in Base.__subclasses__():
                table = self.__session.query(sub_c).all()
                for obj in table:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    result[key] = obj
        return(result)

    def new(self, obj):
        if obj:
            try:
                self.__session.add(obj)

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''closes session'''
        self.__session.close()
