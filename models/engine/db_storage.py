#!/usr/bin/python3
""" module define New engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
import os
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.place import Place
classes = [User, State, City, Amenity, Place, Review]


class DBStorage:
    """
    Intialise Class that represents DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Public instance method"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
                pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Method to retrieve all objects"""
        if cls:
            obj = self.__session.query(cls).all()
            for o in obj:
                k = "{}.{}".format(type(o).__name__, o.id)
                objs[k] = o
        else:
            for c in classes:
                obj = self.__session.query(c).all()
                for o in obj:
                    k = "{}.{}".format(type(o).__name__, o.id)
                    objs[k] = o
        return objs

    def new(self, obj):
        """add ibjet to db"""
        self.__session.add(obj)

    def save(self):
        """
        commit change of database"""
        self.__session.commit()

    def delete(self, obj=None):
        """method the delete from db session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        reloandig database"""
        Base.metadata.create_all(self.__engine)
        ss_f = sessionmaker(bind=self.__engine,
                            expire_on_commit=False)
        Session = scoped_session(ss_f)
        self.__session = Session()

    def close(self):
        """
        Method close session"""
        self.__session.close()
