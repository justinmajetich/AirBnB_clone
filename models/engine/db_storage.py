#!/usr/bin/python3
"""This module defines a Database class to manage file storage"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of engine interface"""
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}\
'.format(user, pswd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retreive all instances for the specified class"""
        instances = {}
        if cls:
            records = self.__session.query(cls).all()
            for row in records:
                key = cls.__name__ + '.' + row.id
                instances[key] = row
        else:
            clases = [State, City]
            for clase in clases:
                records = self.__session.query(clase).all()

                for record in records:
                    key = "{}.{}".format(type(record).__name__, record.id)
                    instances[key] = record
        return instances

    def new(self, obj):
        """Add new object to the database"""
        self.__session.add(obj)

    def save(self):
        """Save changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object fron the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables from metadata inside the database"""
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()
