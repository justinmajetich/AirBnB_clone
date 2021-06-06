#!/usr/bin/python3
"""Module for DBStorage class"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

user = os.environ['HBNB_MYSQL_USER']
passwd = os.environ['HBNB_MYSQL_PWD']
host = os.environ['HBNB_MYSQL_HOST']
database = os.environ['HBNB_MYSQL_DB']
envi = os.getenv('HBNB_ENV')


class DBStorage:
    """"This class manages storage of hbnb models in a MySQL Database"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, passwd, host, database),
                                      pool_pre_ping=True)
        if envi == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects of cls or all objects if None"""
        classes = {
                    'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
        }
        tables = {
                    User: 'users', Place: 'places', State: 'states',
                    City: 'cities', Amenity: 'amenities', Review: 'reviews'
        }
        d = {}
        if not cls:
            tables = Base.__subclasses__()
            for table in tables:
                for instance in self.__session.query(table):
                    key = instance.__class__.__name__ + '.' + instance.id
                    d[key] = instance
        else:
            for instance in self.__session.query(tables[cls]):
                key = instance.__class__.__name__ + '.' + instance.id
                d[key] = instance
        return d

    def new(self, obj):
        """Adds the obj to session"""
        self.__session.add(obj)

    def save(self):
        """Saves session changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from session if it exists"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads the tables from database"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
