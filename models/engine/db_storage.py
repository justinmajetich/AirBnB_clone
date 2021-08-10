#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import Use
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

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
        """Returns a dictionary of models currently in storage"""
        objects = {}
        classes = [City, State, User, Place, Amenity, Review]
        if cls is None:
            list_objs = []
            for idxclass in classes:
                list_objs.extend(self.__session.query(idxclass).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            l_objs = self.__session.query(cls).all()
        for obj in l_objs:
            objects.update({"{}.{}".format(type(obj).__name__, obj.id): obj})
        return objects

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
