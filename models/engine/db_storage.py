#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy import Integer, String, Column, DateTime, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship


class DBStorage:
    """This class manages storage of hbnb models in SQL format"""
    __engine = None
    __session = None

    def __init__(self):
        """Defines the class's instance attributes"""
        usr = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        database = getenv('HBNB_MYSQL_DB')
        host = getenv('HBNB_MYSQL_HOST')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(usr, passwd, host, database),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            classes = [State, City, User, Place, Review, Amenity]
            objs = []
            for c in classes:
                objs += self.__session.query(c).all()
        else:
            objs = self.__session.query(cls).all()
        return {type(obj).__name__ + '.' + obj.id: obj for obj in objs}

    def new(self, obj):
        """Creates a new instance and add it to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def reload(self):
        """Loads storage tables from the database"""
        Base.metadata.create_all(self.__engine)
        db_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(db_session)
        self.__session = Session()
        
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
