#!/usr/bin/python3
""" DB Storage Engine """
from models.base_model import BaseModel, Base
from models.base_model import Amenity
from models.base_model import City
from models.base_model import Place
from models.base_model import Review
from models.base_model import State
from models.base_model import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """ This is our database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize new instance of DBStorage """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects in the current session, optionally filtering by class.
        Returns a dictionary where the keys are in the format <class-name>.<object-id>
        and the values are the corresponding objects.
        """
        objects = {}
        
        if cls is None:
            # Query all types of objects
            for obj_type in [User, State, City, Amenity, Place, Review]:
                for obj in self.__session.query(obj_type):
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        else:
            # Query objects of a specific class
            for obj in self.__session.query(cls):
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        
        return objects


    def new(self, obj):
        """ Add object to current database session """
        self.__session.add(obj)
    
    def save(self):
        """ Commit all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete object from current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_time = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_time)
        self.__session = Session()
