#!/usr/bin/python3
"""DBStorage Engine"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base

user = os.getenv("HBNB_MYSQL_USER")
passwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
data_b = os.getenv("HBNB_MYSQL_DB")
hbnb_env = os.getenv("HBNB_ENV")


class DBStorage():
    """ Engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor method that create a session and engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, data_b),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if (hbnb_env == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method that return a dictionary with all cls objects
            or if cls is None, all objects in the database.
        """
        if type(cls) == str:
            cls = eval(cls)
        mods = [State, City, User, Place, Review]
        if cls is None:
            info = []
            for icls in mods:
                info.extend(self.__session.query(icls).all())  # Make sure!
        else:
            info = self.__session.query(cls)
        return {"{}.{}".format(j.__class__.__name__, j.id): j for j in info}

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Method that delete from the current database
            session obj if not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reload objects from DB"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Method that close de session
        """
        self.__session.close()
