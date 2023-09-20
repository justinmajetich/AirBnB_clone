#!/usr/bin/python3
"""
database storage type
"""

from models.amenity import Amenity
from sqlalchemy import create_engine
from models.base_model import BaseModel Base
from models.state import State
from modesl.city import City
from models.review import Review
from models.place import Place
from models.__init__ import storage
from models.user import User
import sqlalchemy
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """
    database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        create a DBStorage instance
        """
        self.__engine = create_engine()

    def all(self, cls=None):
        """
        retrieve all obj in the db
        """
        my_dict = {}
        if cls is None:
           objects = self.__session.query().all()
           for obj in objects:
               name = obj.__class__.__name__
               key = name + "." + obj.id
               my_dict[key] = obj
            return my_dict
        objects = self.__session.query(cls).all()
        for obj in objects:
            name = obj.__class__.__name__
               key = name + "." + obj.id
               my_dict[key] = obj
            return my_dict

    def new(self, obj):
        '''
        add a new obj to th db
        '''
        self.__session().add(obj)
        self.__session.commit()

    def save(self):
        '''
        save or commit the changes
        '''
        self.__session.commit()

    def delete(self, obj=None):
        """
        deleting an obj fron the db
        """
        if obj is not None:
            self.session.remove(obj)
            self.__session.commit()

        def reload(self):
            """
            reloading the objs from
            the db
            """
            pass

        def close(self):
            """
            doc
            """
            self.__session.remove()
