#!usr/bin/python3
from sqlalchemy import create_engine
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
load_dotenv()


class DBStorage:
    """Database Storage to be used instead of FileStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = __engine
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
        __engine = create_engine(
            'mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306/'
            'hbnb_dev_db',
            pool_pre_ping=True
            )
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        if os.environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        result_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(cls.__name__, obj.id)
                result_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objects = self.__session.query(cls).all()
                for object in objects:
                    key = "{}.{}".format(cls.__name__, object.id)
                    result_dict[key] = object
        return result_dict

    def new(self, obj):
        """add the object to the current database session"""
        return self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        return self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session if obj is not None"""
        if obj is not None:
            return self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
