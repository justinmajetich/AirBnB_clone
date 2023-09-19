#!/usr/bin/python3
"""This module defines a db_storge class"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'),
                                                 getenv('HBNB_MYSQL_PWD'),
                                                 getenv('HBNB_MYSQL_HOST'),
                                                 getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(__engine)

    def all(self, cls=None):
        """get all cls object from mysql"""
        query_results = None
        query_dict = {}
        if cls:
            query_results = self.__session.query(cls).all()
        else:
            query_results = self.__session.query(
                User, State, City, Amenity, Place, Review).all()

        for obj in query_results:
            query_dict[obj.__class__.__name__ + '.' + obj.id] = obj.to_dict()
        return query_dict

    def new(self, obj):
        """add the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        self.__session.delete(obj)

    def reload(self):
        """relod from db"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.base_model import BaseModel, Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
