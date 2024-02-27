#!/usr/bin/python3
"""DataBase Storage Engine Class"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage():
    """This class creates a database engine that will
    store all the created classes in tables
    Attributes:
        __engine: the MySQL DB to be used
        __session: session for the DB
    """
    __engine = None
    __session = None

    def __init__(self):
        """Builder for the engine class"""
        usr = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(usr, passwd, host, db),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Lists all objects of a given class
        or everything if no class is given
        Supports all classes
        """
        objects = {}
        if cls is None:
            classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
            objs = []
            for _class in classes:
                query = self.__session.query(eval(_class))
                for res in query:
                    objs.append(res)
        else:
            objs = self.__session.query(cls).all()
        for value in objs:
            key = type(value).__name__+'.'+str(value.id)
            objects[key] = value
        return objects

    def new(self, obj):
        """Adds a new object to the current session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        "Saves the current session to the database"
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes the object from the current session if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and starts the session"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(ses)
        self.__session = session

    def close(self):
        """Closes the current session"""
        self.__session.remove()
