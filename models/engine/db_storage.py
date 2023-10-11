#!/usr/bin/python3
"""Defintinition for database storgae for airBnB clone"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Class definition for database"""
    __engine = None
    __session = None

    def __init__(self):
        """init function for class"""
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}"
                .format(
                    getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        obj = {}
        if cls is None:
            query_datas = self.__session.query(State).all()
            query_datas.extend(self.__session.query(City).all())
            query_datas.extend(self.__session.query(User).all())
            query_datas.extend(self.__session.query(Place).all())
            query_datas.extend(self.__session.query(Review).all())
            query_datas.extend(self.__session.query(Amenity).all())
        else:
            query_datas = self.__session.query(cls).all()
        for data in query_datas:
            key = f"{type(data).__name__}.{data.id}"
            obj[key] = data
        return obj

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj"""
        if obj is not None:
            try:
                self.__session.delete(obj)
            except Exception as e:
                self.__session.rollback()

    def reload(self):
        """Reload function"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped_Session = scoped_session(Session)
        self.__session = scoped_Session()
