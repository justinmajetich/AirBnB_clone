#!/usr/bin/python3
""" This class defines a DB Storage for the HBNB project"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """Represents a Database Storage
    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new DBStorage object"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the current database session all objects of the given class cls.
        If cls is None, queries all types of objects.
        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        new_dict = {}
        for c in classes:
            if cls is None or cls is classes[c] or cls is c:
                objects = self.__session.query(classes[c]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

#        if cls is None:
#            objects = self.__session.query(State).all()
#            objects.extend(self.__session.query(City).all())
#            objects.extend(self.__session.query(User).all())
#            objects.extend(self.__session.query(Amenity).all())
#            objects.extend(self.__session.query(Place).all())
#            objects.extend(self.__session.query(Review).all())
#        else:
#            if type(cls) == str:
#                cls = eval(cls)
#            objects = self.__session.query(cls)
#        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """ add the object to the current database session """
        local_obj = self.__session.merge(obj)
        self.__session.add(local_obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database and initialize a new session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ close the current SqlAlchemy session """
        self.__session.close()
