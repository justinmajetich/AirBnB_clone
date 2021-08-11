#!/usr/bin/python3
""" New engine """
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
        # create engine with args from input
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, data_b),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        # use the test env if required
        if (hbnb_env == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method that return a dictionary with all cls objects
            or if cls is None, all objects in the database.
        """
        # check the class from input
        if type(cls) == str:
            cls = eval(cls)
        classes = [State, City, User, Place, Review]
        if cls is None:
            # lobj == list_objects
            lobj = []
            for idx_classes in classes:
                lobj.extend(self.__session.query(idx_classes).all())
        else:
            lobj = self.__session.query(cls)
        return {
            "{}.{}".format(obj.__class__.__name__, obj.id): obj for obj in lobj
            }

    # ORM methods... check documentation of SQLAlchemy
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

    #
    def reload(self):
        """ Reload objects from DB"""
        # check the documentation for sessionmaker
        # open the engine
        Base.metadata.create_all(self.__engine)
        # open session
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        # use scoped session
        # __session is an instance of Session
        self.__session = Session()

    def close(self):
        """ Method that close a session. """
        self.__session.close()
