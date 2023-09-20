#!/usr/bin/env python3
"""This module defines a class to manage db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State, Base
from models.city import City, Base
from models.review import Review


usr = getenv('HBNB_MYSQL_USER')
pwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
status = getenv('HBNB_ENV')


class DBStorage:
    """ This class manages the db storage"""
    __engine =  None
    __session = None

    def __init__(self):
        """Initialise DB"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db),
            pool_pre_ping=True)

        if status == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Get all object of specific class or all classes"""

        allCls = [State, City, Place]

        output = {}
        if cls is None:
            for unit_cls in allCls:
                for value in self.__session.query(unit_cls).all():
                    key = value.__class__.__name__ + '.' + value.id
                    output[key] = value
        else:
            for value in self.__session.query(cls).all():
                key = value.__class__.__name__ + '.' + value.id
                output[key] = value

        return output

    def new(self, obj):
        """Add new object"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Save current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload storage"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(SessionFactory)
        self.__session = Session()
