#!/usr/bin/python3
""" This module creates an engine for saving to database """
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User

""" Setting env variables """
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_ENV = os.getenv('HBNB_ENV')

classdict = {'User': User,
             'State': State,
             'City': City,
             # 'Amenity': Amenity,
             'Place': Place,
             # 'Review': Review
             }


class DBStorage:
        """ Class to run database engine """
        __engine = None
        __session = None

        def __init__(self):
                """ Initializes class """
                self.__engine = create_engine(
                        'mysql+mysqldb://{}:{}@{}/{}'.format(
                                HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                        pool_pre_ping=True)

                # Drop all tables if env is test
                if HBNB_ENV == 'test':
                        Session = sessionmaker(
                                bind=self.__engine, expire_on_commit=False)
                        session_scoped = scoped_session(Session)
                        self.__session = session_scoped()
                        Base.metadata.create_all(self.__engine)

        def all(self, cls=None):
                """ query on the current database session (self.__session)
                all objects depending of the class name (argument cls);
                returns dict """
                self.reload()
                for key, value in classdict.items():
                        retdict = {}
                        if cls is None or cls == key:
                                for u in self.__session.query(
                                        classdict[key]).all():
                                        k = u.__class__.__name__ + "." + u.id
                                        retdict[k] = u
                        return retdict

        def reload(self):
                """ creates all tables in the database """
                Session = sessionmaker(
                        bind=self.__engine, expire_on_commit=False)
                session_scoped = scoped_session(Session)
                self.__session = session_scoped()
                Base.metadata.create_all(self.__engine)

        def new(self, obj):
                """ add the object to the current database session """
                # Needs to create an instance before saving it
                print("In new")
                for key, value in classdict.items():
                        if key == obj:
                                new = value(name="Placeholder")
                self.__session.add(new)
                print("New item is {}".format(new))
                self.save()
                return new()

        def save(self):
                """ Commits all changes of the current database session """
                self.__session.commit()

        def delete(self, obj=None):
                """ Deletes from current session if obj not None """
                if obj is not None:
                        self.__session.delete(obj)
                self.save()
