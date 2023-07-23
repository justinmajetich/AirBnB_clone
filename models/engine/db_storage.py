#!/usr/bin/python3
"""New engine DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """a class for the new engine"""
    __engine = None
    __session = None

    def __init__(self):
        """creates the engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary"""
        dct = {}
        if cls:
            objects = self.__session.query(cls)
            for obj in objects:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dct[key] = obj
        else:
            c_list = [State, City, User, Place, Review, Amenity]
            for cl in c_list:
                objects = self.__session.query(cl)
                for obj in objects:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dct[key] = obj

        return dct

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not none"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates in the database and creates the database session"""
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(
                sessionmaker(
                    bind=self.__engine,
                    expire_on_commit=False
                )
        )
        self.__session = Session()

    def close(self):
        """call remove() method on the privte session attri(self.__session)"""
        self.__session.remove()
