#!usr/bin/python3
from sqlalchemy import create_engine
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DBStorage:
    """Database Storage to be used instead of FileStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = __engine
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                        expire_on_commit=False))
        __engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306/hbnb_dev_db',
                                 pool_pre_ping=True)
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'
        if os.environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query on the current database session"""
        if cls is not None:
            return self.__session.query(cls).all()
        else:
            return self.__session.query(State).all() + self.__session.query(City).all() + self.__session.query(User).all() + self.__session.query(Place).all() + self.__session.query(Review).all() + self.__session.query(Amenity).all()
        return dict
        