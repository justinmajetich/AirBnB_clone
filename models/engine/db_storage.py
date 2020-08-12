#!/usr/bin/python3
"""DB engine storage module """

import os
import MySQLdb
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {'User': User, 'Place': Place,
             'State': State, 'City': City, 'Amenity': Amenity,
             'Review': Review
           }


class DBStorage:
    """DBStorage class definition"""

    __engine = None
    __session = None

    def __init__(self):
        """Create engine linked to db"""
        user = os.getenv('HBNB_MYSQL_USER')
        pswd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST ')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                               user, pswd, host, db), pool_pre_ping = True)
        if os.getenv('HBNB_ENV') == 'test':
            # drop all tables
            pass

    def all(self, cls = None):
        """Query currend tb session for all objects dpending on cls"""
        show={}
        for clase in classes:
            if cls is None or cls is classes[clase] or cls is clase:
                objects = self.__session.query(clase).all()
                for obj in objects:
                    show[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return show

    def new(self, obj):
        """Add the obj to the current db session"""
        self.__session.add(obj)

    def save(self):
        """commit al changes of the current db session"""
        self.__session.commit()

    def delete(self, obj = None):
        """delete obj from the current dn if not None"""
        self.__session.delete(obj)

    def reload(self):
        """create all tables in database, create current db session"""
        Base.metadata.create_all(self.__engine)

        session_factory=sessionmaker(
            bind = self.__engine, expire_on_commit = False)
        Session=scoped_session(session_factory)
        self.__session=Session()
