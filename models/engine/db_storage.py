#!/usr/bin/env python3
"""This module defines a class to manage db storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


usr = os.environ.get('HBNB_MYSQL_USER')
pwd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
status = os.environ.get('HBNB_ENV')


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
        """a public instance method that returns a dictionary
        consisting of all queried class from the database"""
        from models.amenity import Amenity
        from models.user import User
        from models.place import Place
        from models.state import State, Base
        from models.city import City, Base
        from models.review import Review

        if cls is None:
            cls = [State, City, User, Place, Review, Amenity]
            query = []
            for c in cls:
                query.extend(self.__session.query(c).all())
        else:
            query = self.__session.query(cls).all()
        cls_objs = {}
        for obj in query:
            cls_objs[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return cls_objs

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
