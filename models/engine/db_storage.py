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
                print(self.__engine)

                # Drop all tables if env is test
                if HBNB_ENV == 'test':
                        Base.metadata.drop_all(self.__engine)
                        print("Env is test")
                
        def all(self, cls=None):
                """ query on the current database session (self.__session) all objects depending of the class name (argument cls); returns dict """
                print("In all")
                if cls == None:
                        # equal to show all?
                        print("Not yet set up")
                        """for instance in session:
                                print("{}: {}".format(instance.id, instance.name))"""
                else:
                        for instance in self.__session.query(State).order_by(State.id):
                                print("{}: {}".format(instance.id, instance.name))
                        # query based on cls

        def reload(self):
                """ creates all tables in the database """
                Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
                session_scoped = scoped_session(Session)
                self.__session = session_scoped()
                Base.metadata.create_all(self.__engine)
