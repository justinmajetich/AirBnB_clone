#!/usr/bin/python3
""" db storage engine """
import sys
import os
from models.base_model import BaseModel as base, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)


class DBStorage:
    """ The db storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ init function """
        host = os.getenv('HBNB_MYSQL_HOST')
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all()

    def all(self, cls=None):
        """ query all data """
        from models.state import State
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place
        classes = {'User': User, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review}

        if not self.__session:
            Session = sessionmaker()
            Session.configure(bind=self.__engine, expire_on_commit=False)
            sess = scoped_session(Session)
            self.__session = sess()

        objs = {}

        if cls and issubclass(cls, base):
            query = self.__session.query(cls).all()
            for obj in query:
                objs.update({str(obj.__class__.__name__) + '.' + obj.id: obj})
        elif cls is None:
            for k, v in DBStorage.classes:
                query = self.__session.query(v).all()
                for obj in query:
                    objs.update({str(obj.__class__.__name__) +
                                 '.' + obj.id: obj})
        return objs

    def new(self, obj):
        """ create a new obj """
        Session = sessionmaker()
        Session.configure(bind=self.__engine)
        self.__session = Session()
        if obj and isinstance(obj, base):
            self.__session.add(obj)

    def save(self):
        """ commit all changes of current session """
        if self.__session is not None:
            self.__session.commit()
            self.__session.close()

    def close(self):
        """ close session """
        self.__session.remove()

    def delete(self, obj=None):
        """ delete obj if not none from session """
        if obj and isinstance(obj, base):
            self.__session.delete(obj)

    def reload(self):
        """ reload all tables and data """
        from models.state import State
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        Base.metadata.create_all(self.__engine)
        if self.__session:
            self.__session.close_all()
        s_f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_f)
        self.__session = Session()
