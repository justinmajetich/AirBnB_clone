#!/usr/bin/python3

"""
A database storage engine
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DBSTORAGE:
    """
    Represents a database storage engine

    Attributes:
    __engine: refers to the sqlAlchemy engine
    __session: the session of the aqlalchemy
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializing a new database storage instance
        """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                        pool_pre_ping=True)
        """ drop all tables if the environment variable HBNB_ENV is equal to test """
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session (self.__session) all objects
        depending of the class name (argument cls)
        if cls=None, query all types of objects
        (User, State, City, Amenity, Place and Review)

        Return:
        a dictionary: (like FileStorage)
        key = <class-name>.<object-id>
        value = object
        """
        if cls is None:
            """ If cls is not specified, query for objects of all types """
            objects = self.session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        else:
            """If the class is specified, look for objects in that class"""
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
            """
             Create a dictionary where keys are in the format <class-name>.<object-id>
             and values are the corresponding objects
            """
            return {"{}.{}".format(type(h).__name, h.id): h for h in objects}

    def new(self, obj=None):
        """
        add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """Commits(saves) all changes made to the current database session"""
        self.__session.commit

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and start a new session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the sqlalchemy session"""
        self.__session.close()
