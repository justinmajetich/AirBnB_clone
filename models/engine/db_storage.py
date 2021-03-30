#!/usr/bin/python3
""" This module use mysql database """
from sqlalchemy import create_engine
from models.state import Base
from sqlalchemy.orm import Session, sessionmaker, scoped_session
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ constructor """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                os.environ.get('HBNB_MYSQL_USER'),
                os.environ.get('HBNB_MYSQL_PWD'),
                os.environ.get('HBNB_MYSQL_HOST'),
                os.environ.get('HBNB_MYSQL_DB'),
            ),
            pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        self.reload()

    def all(self, cls=None):
        """ class all """
        class_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

        dict_class = {}
        if cls is None:
            obj_list = []
            for class_name in class_list:
                obj_list = self.__session.query((class_name).all())
                if len(obj_list) > 0:
                    for obj in obj_list:
                        key = class_name + '.' + obj.__dict__['id']
                        dict_class[key] = obj
            return dict_class
        else:
            obj_list = self.__session.query(cls).all()
            if len(obj_list) > 0:
                for obj in obj_list:
                    key = type(obj).__name + '.' + obj.__dict__['id']
                    dict_class[key] = obj
            return dict_class

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ remove the object from the current database session """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)

        
        current_session = sessionmaker(
            bin=self.__session, expire_on_commit=False)
        self.__session = scoped_session(current_session)
