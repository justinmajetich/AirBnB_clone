#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
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

# save the data for the access to the databases in the engine
user = os.getenv("HBNB_MYSQL_USER")
passwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
data_b = os.getenv("HBNB_MYSQL_DB")
hbnb_env = os.getenv("HBNB_ENV")


class DBStorage:
    """This class manages storage of hbnb models in a mysql database"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor method that create a session and engine"""
        # link the orm with the databases
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, data_b),
                                      pool_pre_ping=True)
        # start the engine
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

    # ORM methods... check documentation of SQLAlchemy
    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        # saves the changes on a sql database
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload objects from DB"""
        Base.metadata.create_all(self.__engine)
        # check for sessionamker docs
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        # check for scoped_session docs
        Session = scoped_session(session_factory)
        # __session is an instance of Session
        self.__session = Session()
        """
        This pattern allows disparate sections of the
        application to call upon a global scoped_session,
        so that all those areas may share the same session
        without the need to pass it explicitly. The Session
        we’ve established in our registry will remain, until
        we explicitly tell our registry to dispose of it,
        by calling scoped_session.remove()
        The job of the scoped_session is simple;
        hold onto a Session for all who ask for it.
        """

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
