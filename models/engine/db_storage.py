#!/usr/bin/python3
"""DBStorage Engine"""
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ New engine DBStorage
    Private class attributes engine and session """
    __engine = None
    __session = None

    def __init__(self):
        """ initialization for DBStorage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ List all the objects from a passed class, if None then
        list all the classes with respective objects as a dict"""
        object_cls = {}
        query_sum = []
        if cls:
            if cls is str:
                quer = self.__session.query(eval(cls)).all()
            else:
                quer = self.__session.query(cls).all()
            query_sum.extend(quer)
        else:
            classes = ['State', 'City', 'User', 'Place', 'Review']
            for clas in classes:
                if cls is str:
                    quer = self.__session.query(eval(clas)).all()
                else:
                    quer = self.__session.query(clas).all()
                query_sum.extend(quer)
        for instance in query_sum:
            if cls is str:
                key = cls + '.' + instance.id
            else:
                key = cls.__name__ + '.' + instance.id
            object_cls[key] = instance
        return object_cls

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self, obj=None):
        """ delete from the current database session obj if not None """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """ method used for sesssion closing """
        self.__session.close()