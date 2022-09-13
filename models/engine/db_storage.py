#!/usr/bin/python3
""" Defines the Database Storage"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.base_model import Basemodel, Base
from os import getenv
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker, scoped_session


class DBStorage:
    """Represents a Database Storage engine
    Attributes:
        __engine (sqlalchemy.engine): The working sqlalchemy engine
        __session (sqlalchemy.session): The working sqlalchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new Database storage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PASSWORD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session (self.__session) all objects 
        depending of the class name (argument cls)

        If class is None, Queries all types of objects

        Return:
            Dict of Queried classes in format <class-name>.<object-id> = obj
        """

        if cls is None:
            objs = self.__session.query(State).all()
            classes_lists = [City, User, Place, Review, Amenity]
            for clasname in classes_lists:
                objs.extend(self.__session.query(clasname).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        return {'{}.{}'.format(type(obj).__name__, obj.id) for obj in objs}

    def new(self, obj):
        """Add obj to the current database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in database and initializes a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the working session"""
        self.__session.close()
