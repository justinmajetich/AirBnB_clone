#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = (
            create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                          .format(getenv('HBNB_MYSQL_USER'),
                                  getenv('HBNB_MYSQL_PWD'),
                                  getenv('HBNB_MYSQL_HOST'),
                                  getenv('HBNB_MYSQL_DB')
                                  ), pool_pre_ping=True)
                            )
        
        # drop all tables if the environment variable HBNB_ENV is equal to test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current db all objects depending on the class name."""
        from models import classes

        result_dict = {}

        if cls:
            if isinstance(cls, str) and (class_obj := classes.get(cls)):
                query = self.__session.query(class_obj).all()
                # Return a dictionary: (like FileStorage)
                return {"{}.{}".format(cls, elem.id): elem for elem in query}
            else:
                # provided cls not found in classes
                return result_dict

        # If cls is not provided, iterate through all classes
        for class_name, class_object in classes.items():
            query = self.__session.query(class_object)
            for elem in query:
                key = "{}.{}".format(class_name, elem.id)
                result_dict[key] = elem

        return result_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)