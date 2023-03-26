#!/usr/bin/pyhton

from models.base_model import Base
from models.base_model import BaseModel
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ Private Instance Attributes for DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initialization of DBStorage """
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_pwd =  os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db_name = os.getenv('HBNB_MYSQL_DB')
        db_env = os.getenv('HBNB_ENV')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
				      .format(db_user, db_pwd, db_name),\
				      pool_pre_ping=True)
        if db_env == "test":
           Base.metadata.dropall(self.__engine)

    Session = sessionmaker(bind=self.__engine)
    self.__session = Session()

    def all(self, cls=None):
        """ query cls object
            and return dictionary of 
            key: <classname>.<object_id>
            value: object"""
        if cls is not None:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()

        else:
            objs = self.__session.query(User).all()
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())

        dictionary = {}
        for i in range(len(objs)):
            key = "{}.{}".format(type(objs[i]).__name__, objs[i].id)
            dictionary[key] = objs[i]

        return dictionary

    def new(self, obj):
        """ Add new data/object in database session """
        self.__session.add(obj)

    def save(self):
        """ Commit/save newly added object """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
